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
    <!-- FILTER FEATURE -->

    <b-row>
      <b-col lg="6" class="my-1">
        <b-form-group
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          label-for="sortBySelect"
          class="mb-0"
        ></b-form-group>
      </b-col>

      <b-col lg="6" class="my-1">
        <b-form-group
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          label-for="initialSortSelect"
          class="mb-0"
        ></b-form-group>
      </b-col>

      <b-col lg="6" class="my-1">
        <b-form-group
          label="Filter"
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          label-for="filterInput"
          class="mb-0"
        >
          <b-input-group size="sm">
            <b-form-input
              v-model="filter"
              type="search"
              id="filterInput"
              placeholder="Type to Search"
            ></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>
          </b-input-group>
          <b-input-group size="sm" v-if="false">
            <b-form-select v-model="filter" size="sm" :options="filterOption"></b-form-select>
          </b-input-group>
        </b-form-group>
      </b-col>

      <b-col lg="6" class="my-1">
        <b-form-group
          label="Filter On"
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          description="Leave all unchecked to filter on all data"
          class="mb-0"
        >
          <b-form-checkbox-group v-model="filterOn" class="mt-1">
            <b-form-checkbox value="GadgetName">GadgetName</b-form-checkbox>
            <b-form-checkbox value="Status">Status</b-form-checkbox>
            <b-form-checkbox value="PurchasedDate">Purchased Date</b-form-checkbox>
            <b-form-checkbox value="RoomName">Room Name</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
      </b-col>

      <b-col sm="5" md="6" class="my-1">
        <b-form-group
          label="Per page"
          label-cols-sm="6"
          label-cols-md="4"
          label-cols-lg="3"
          label-align-sm="right"
          label-size="sm"
          label-for="perPageSelect"
          class="mb-0"
        >
          <b-form-select v-model="perPage" id="perPageSelect" size="sm" :options="pageOptions"></b-form-select>
        </b-form-group>
      </b-col>

      <b-col sm="7" md="6" class="my-1">
        <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          align="fill"
          size="sm"
          class="my-0"
        ></b-pagination>
      </b-col>
    </b-row>

    <div v-if="isLoading" class="w-100 my-5 d-flex align-items-center justify-content-center">
      <div class="pr-3">
        <i class="fas fa-circle-notch fa-spin fa-2x"></i>
      </div>
      <div>
        <strong style="font-size: 24px">Loading...</strong>
      </div>
    </div>

    <!-- End of Filter form -->
    <b-table
      :items="gadgets"
      :fields="fields"
      striped
      responsive="sm"
      :current-page="currentPage"
      :per-page="perPage"
      :filter="filter"
      :filterIncludedFields="filterOn"
      :sort-by.sync="sortBy"
      :sort-desc.sync="sortDesc"
      :sort-direction="sortDirection"
      @filtered="onFiltered"
      id="table-transition-example"
      :tbody-transition-props="transProps"
    >
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
      fields: [
        { key: "GadgetName", sortable: true },
        { key: "Status", sortable: false },
        { key: "PurchasedDate", sortable: true },
        { key: "RoomName", sortable: false },
        "Manage"
      ],
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
      currentPage: 1,
      perPage: 5,
      pageOptions: [1, 5, 10, 15],
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      filter: null,
      filterOn: [],
      transProps: {
        // Transition name
        name: "flip-list"
      },
      filterOption: [],
      allRoomNames: [],
      IsTypeToSearch: true
    };
  },
  computed: {
    ...mapState({
      isLoading: state => state.room.isLoading,
      isSuccess: state => state.room.isSuccess,
      isError: state => state.room.isError,
      gadgets: state => {
        // alert("vuex gadget update")
        return state.room.gadgets;
      },
      rooms: state => state.room.rooms,
      roomTypes: state => Object.keys(state.room.rooms),
      roomNames: state => state.room.roomNames,
      totalRows: state => state.room.gadgets.length
    }),
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter(f => f.sortable)
        .map(f => {
          return {
            text: f.label,
            value: f.key
          };
        });
    }
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
          this.newGadget.Room_id = this.rooms[this.roomType][this.roomName];
        }
      }
    }
    // filterOn: function() {
    //   if (this.filterOn.includes("Status") && this.filterOn.length === 1) {
    //     this.IsTypeToSearch = false;
    //     this.filterOption.push("Available", "NotAvailable");
    //   } else {
    //     this.IsTypeTosearch = true;
    //     this.filterOption = this.filterOption.filter(mem => {
    //       return mem != "Available" && mem != "NotAvailable";
    //     });
    //   }
    //   if (this.filterOn.includes("RoomName") && this.filterOn.length === 1) {
    //     this.IsTypeToSearch = false;
    //     this.filterOption.concat(this.allRoomNames);
    //   } else {
    //     this.IsTypeTosearch = true;
    //     this.filterOption = this.filterOption.filter(mem => {
    //       return !this.allRoomNames.includes(mem);
    //     });
    //   }
    // }
  },

  methods: {
    onFiltered(filteredItems) {
      totalRows = filteredItems.length;
      this.currentPage = 1;
    },
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
      if (this.action == "ADD") {
        this.newGadget.Status = "Available";
      } else {
        //UPDATE
        this.newGadget.Room_id = this.rooms[this.roomType][this.roomName];
        this.newGadget.Status = this.available;
        this.newGadget;
      }
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
    deletedGadget: function(id) {
      // get data
      this.$store.dispatch("room/deleteGadget", id);
    },
    fetchUpdatedData: function(item) {
      // console.log(item)
      this.action = "UPDATE";
      this.roomType = item.RoomType;
      this.roomName = item.RoomName;
      this.roomName = item.RoomName;
      this.available = item.Status;
      this.gadgetName = item.GadgetName;
      let stringDate = item.PurchasedDate;
      //setting newGadget id
      this.newGadget.id = item.GadgetID;
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
            // alert(item.GadgetID)

            this.deletedGadget(item.GadgetID);
          } else {
            // asdasda
          }
        });
    }
  },
  mounted() {
    this.fetchGadgets();
    this.fetchRooms();
    for (roomType in this.roomTypes) {
      this.allRoomNames.concat(Object.keys(this.rooms[roomType]));
    }
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

table#table-transition-example .flip-list-move {
  transition: transform 1s;
}
</style>
