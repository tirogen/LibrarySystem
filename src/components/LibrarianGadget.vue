<template>
  <div class="jumbotron bg-overlay">
    <h2>
      Gadget
      <b-button v-b-modal.modal-1 @click="showGadgetModal()">ADD GADGET</b-button>
    </h2>
    <!-- Add GadGet Modal -->
    <div>
      <b-modal id="modal-1" v-model="show" title="ADD GADGET">
        <b-container fluid class="bv-example-row bv-example-row-flex-cols">
          <b-row class="mb-1 text-center" align-v="start">
            <b-col cols="1.7"></b-col>
            <b-col>RoomType</b-col>
            <b-col>RoomName</b-col>
          </b-row>
          <b-row class="mb-1">
            <b-col cols="1.5">Room</b-col>
            <b-col>
              <b-form-select v-model="roomType" :options="roomTypes" required></b-form-select>
            </b-col>
            <b-col>
              <b-form-select v-model="roomName" :options="roomNames" required></b-form-select>
            </b-col>
          </b-row>
          <b-row class="mb-1">
            <b-col cols="1.5" class>Gadget Name</b-col>
            <b-col>
              <b-form-input id="name-input" v-model="gadgetName" required></b-form-input>
            </b-col>
          </b-row>
          <b-row v-if="this.action=='UPDATE'">
            <b-col cols="1.5" class>Available Status</b-col>
            <b-col>
              <b-form-select v-model="available" :options="statuses"></b-form-select>
            </b-col>
          </b-row>
          <b-row class="mb-1">
            <b-col cols="4.5" class>Purchase Date</b-col>
            <b-col class="text-center">
              <datepicker
                :format="customFormatter"
                v-model="cal.date"
                :language="th"
                :disabled-dates="cal.disabledDates"
                name="uniquename"
              ></datepicker>
            </b-col>
          </b-row>
          <b-row align-h="start">
            <b-col>CLICK BOX TO CHANGE PURCHASE DATE</b-col>
          </b-row>
        </b-container>
        <template v-slot:modal-footer>
          <div class="w-100">
            <!-- <p class="float-left">Submit to add gadget</p> -->
            <b-button variant="primary" size="sm" class="float" @click="checkAction()">CONFIRM</b-button>
            <b-button variant="primary" size="sm" class="float-right" @click="show=false">CANCEL</b-button>
          </div>
        </template>
      </b-modal>
    </div>
    <!-- End of add Gadget modal -->
    <b-table :items="gadgets" :fields="fields" striped responsive="sm">
      <template v-slot:cell(Manage)="row">
        <b-button
          size="sm"
          @click="row.toggleDetails"
          class="mr-2"
        >{{ row.detailsShowing ? 'Hide' : 'Show'}} Manage</b-button>
      </template>
      <template v-slot:row-details="row">
        <b-card>
          <b-button
            size="sm"
            v-b-modal.modal-1
            variant="primary"
            class="m-2"
            @click="fetchUpdatedData(row.item)"
          >Update</b-button>
          <b-button
            size="sm"
            variant="danger"
            class="m-2"
            @click="showDeleteConfirm(row.item)"
          >Delete</b-button>
        </b-card>
      </template>
    </b-table>
    <b-button block variant="primary">See all</b-button>
  </div>
</template>
<script>
import { mapState } from "vuex";
import Datepicker from "vuejs-datepicker";
import { en, th } from "vuejs-datepicker/dist/locale";

export default {
  name: "Gadget",
  props: {},
  data() {
    return {
      statuses: ["Available", "NotAvailable"],
      action: "ADD",
      en: en,
      th: th,
      cal: {
        date: new Date(),
        disabledDates: {
          // to: new Date(), // Disable all dates up to specific date
          from: new Date() // Disable all dates after specific date
          // days: [6, 0], // Disable Saturday's and Sunday's
          // daysOfMonth: [29, 30, 31], // Disable 29th, 30th and 31st of each month
          // dates: [ // Disable an array of dates
          //   new Date(2016, 9, 16),
          //   new Date(2016, 9, 17),
          //   new Date(2016, 9, 18)
          // ],
          // ranges: [{ // Disable dates in given ranges (exclusive).
          //   from: new Date(2016, 11, 25),
          //   to: new Date(2016, 11, 30)
          // }, {
          //   from: new Date(2017, 1, 12),
          //   to: new Date(2017, 2, 25)
          // }],
          // a custom function that returns true if the date is disabled
          // this can be used for wiring you own logic to disable a date if none
          // of the above conditions serve your purpose
          // this function should accept a date and return true if is disabled
          // customPredictor: function(date) {
          //   // disables the date if it is a multiple of 5
          //   if(date.getDate() % 333 == 0){
          //     return true
          //   }
          // }
        }
      },
      gadgetName: "",
      fields: ["GadgetName", "Status", "PurchasedDate", "RoomName", "Manage"],
      newGadget: {
        id: null,
        Name: null,
        Status: null,
        PurchasedDate: null,
        Room_id: null
      },
      show: false,
      roomName: "",
      roomType: "",
      available: null,
      nameOption: "",
      deletedid: ""
    };
  },
  computed: {
    ...mapState({
      isLoading: state => state.room.isLoading,
      isSuccess: state => state.room.isSuccess,
      isError: state => state.room.isError,
      gadgets: state => state.room.gadgets,
      rooms: state => state.room.rooms,
      roomTypes: state => Object.keys(state.room.rooms),
      roomNames: state => state.room.roomNames
    })
  },
  watch: {
    roomType: function() {
      if (this.action == "ADD") {
        this.$store.dispatch("room/fetchRoomNames", this.roomType);
      } else if (this.action == "UPDATE" && this.roomType != "") {
        // check roomType in key
        // this.rooms[]
        // if (this.roomName == "") {
        this.$store.dispatch("room/fetchRoomNames", this.roomType);
        // }
      }
      //  this.roomNames = Object.keys(dat[this.roomType])
    },
    roomName: function() {
      if (this.action == "ADD") {
        this.newGadget.Room_id = this.rooms[this.roomType][this.roomName];
      } else if (this.action == "UPDATE") {
        if (this.roomName == "" && this.roomType != "") {
          // this.$store.dispatch("room/fetchRoomNames", this.roomType);
        }
      }
    }
  },

  methods: {
    checkAction: function() {
      if (this.action == "ADD") {
        this.addGadget();
      } else if (this.action == "UPDATE") {
        this.updateGadget();
      }
    },
    customFormatter(date) {
      let mo = date.getMonth() + 1;
      if (mo <= 9) {
        var m = "0" + mo;
      } else {
        m = mo;
      }
      let dd = date.getDate();
      if (dd <= 9) {
        var d = "0" + dd;
      } else {
        d = dd;
      }
      let dateFormat = date.getFullYear() + "-" + m + "-" + d;
      this.newGadget.PurchasedDate = dateFormat;
      return dateFormat;
    },
    fetchGadgets: function() {
      this.$store.dispatch("room/fetchGadgets");
    },
    addGadget: function() {
      this.handleGadget();
      this.handleGadgetValue().then(success => {
        if (success) {
          this.show = false;

          this.$store.dispatch("room/postGadget", this.newGadget);
          //animate View
        } else {
          alert("data is not valid");
        }
      });
    },
    showGadgetModal: function() {
      this.action = "ADD";
      //show modal true
      this.show = true;
      this.fetchRooms();
    },
    fetchRooms: function() {
      this.$store.dispatch("room/fetchRooms");
    },
    //setting newGadget
    handleGadget: function() {
      this.newGadget.Name = this.gadgetName;
      this.newGadget.Status = "Available";
      // this.newGadget.id = this.
      // this.newGadget.PurchasedDate = this.date >> does in customFormat already bind
      // console.log(this.newGadget);
    },
    handleGadgetValue: async function() {
      // check form is valid
      if (
        this.roomName === "" ||
        this.roomType === "" ||
        this.gadgetName === ""
      ) {
        return false;
        // need to check format
      }
      //
      return true;
    },
    deletedGadget: function() {
      // get data
      // this.$store.dispatch("room/deleteGadget", this.deletedid);
    },
    fetchUpdatedData: function(item) {
      this.action = "UPDATE";
      this.roomType = item.RoomType;
      this.roomName = item.RoomName;
      this.roomName = item.RoomName;
      this.available = item.Status;
      this.gadgetName = item.GadgetName;
      let stringDate = item.PurchasedDate;
      //setting newGadget id
      this.newGadget.id = item.id
      // alert(stringDate)
      let arr = stringDate.split("-");
      // alert(arr)
      this.cal.date = new Date(arr[0], parseInt(arr[1]) - 1, arr[2]);
      this.show = true;
    },
    updateGadget: function() {
      this.handleGadget();
      this.handleGadgetValue().then(success => {
        if (success) {
          this.show = false;
          this.$store.dispatch("room/updateGadget", this.newGadget);
          //animate View
        } else {
          alert("data is not valid to update");
        }
      });
    },
    showDeleteConfirm(item) {
      this.$bvModal
        .msgBoxConfirm("Please confirm that you want to delete.", {
          title: "Please Confirm",
          size: "sm",
          buttonSize: "sm",
          okVariant: "danger",
          okTitle: "YES",
          cancelTitle: "NO",
          footerClass: "p-2",
          hideHeaderClose: false,
          centered: true
        })
        .then(value => {
          if (value) {
            // alert(Object.keys(item))
            alert(item.GadgetID)
            // this.deletedGadget(item);
          } else {
            // asdasda
          }
        });
    }
  },
  mounted() {
    this.fetchGadgets();
    this.fetchRooms();
  },
  components: {
    Datepicker
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

img {
  width: 250px;
}
/* .colBackground{
    background-color: lightseagreen;
} */
</style>
