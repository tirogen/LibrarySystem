<template>
  <div class="jumbotron bg-overlay">
    <h2>Gadget
      <b-button v-b-modal.modal-1 @click="fetchRooms()">ADD GADGET</b-button>
    </h2>
    <!-- Add GadGet Modal -->
    <div>
      <b-modal
        id="modal-1"
        v-model="show"
        title="ADD GADGET"
      >
        <b-container fluid>
          <div>
            <b-row class="mb-1 text-center">
              <b-col cols="1.7"></b-col>
              <b-col>RoomName</b-col>
              <b-col>RoomType</b-col>
            </b-row>
            
        <b-row class="mb-1">
          <b-col cols="1.5">Room</b-col>
          <b-col>
            <b-form-select
              v-model="roomType"
              :options="roomTypes"
            ></b-form-select>
          </b-col>
          <b-col>
            <b-form-select
              v-model="roomName"
              :options="roomNames"
            ></b-form-select>
          </b-col>
        </b-row>
        </div>

          <b-row class="mb-1 pad">
            <b-col cols="1.5" class="pad">Gadget Name</b-col>
            <b-col>
              <b-form-input
                id="name-input"
                v-model="gadgetName"
                required
              ></b-form-input>
            </b-col>
          </b-row>
        </b-container>
        <template v-slot:modal-footer>
          <div class="w-100">
            <!-- <p class="float-left">Submit to add gadget</p> -->
             <b-button
              variant="primary"
              size="sm"
              class="float"
              @click="addGadget()"
            >
              CONFIRM
            </b-button>
            <b-button
              variant="primary"
              size="sm"
              class="float-right"
              @click="show=false"
            >
              CANCEL
            </b-button>
          </div>
        </template>
      </b-modal>
    </div>
    <!-- End of add Gadget modal -->
    <b-table :items="gadgets" :fields="fields" striped responsive="sm">
      <template v-slot:cell(Manage)="row">
        <b-button size="sm" @click="row.toggleDetails" class="mr-2">
          {{ row.detailsShowing ? 'Hide' : 'Show'}} Manage
        </b-button>
      </template>
      <template v-slot:row-details="row">
        <b-card>
          <b-button size="sm" variant="primary" class="m-2">Check in</b-button>
          <b-button size="sm" variant="danger" class="m-2">Delete</b-button>
        </b-card>
      </template>
    </b-table>
    <b-button block variant="primary">See all</b-button>
  </div>
</template>

<script>
import {mapState} from 'vuex';

export default {
  name: 'Gadget',
  props: {},
  data() {
    return {
      gadgetName: "",
      fields: ['GadgetName', 'Status', 'PurchasedDate', 'RoomName', 'Manage'],
      newGadget: {'Name': null, 'Status': null, 'PurchasedDate': null, 'Room_id': null},
      show: false,
      roomName: "",
      roomType: "",
      nameOption: "" 
    }
  },
  computed: mapState({
    isLoading: state => state.room.isLoading,
    isSuccess: state => state.room.isSuccess,
    isError: state => state.room.isError,
    gadgets: state => {
      return state.room.gadgets
    },
    rooms: state => {
      return state.room.rooms;
    },
    roomTypes: state=> {
      return Object.keys(state.room.rooms)
    },
    roomNames: (state) => {
      return state.room.roomNames
    }
  })
  ,
  watch: {
     roomType: function() {
      this.$store.dispatch('room/fetchRoomNames',this.roomType)
      //  this.roomNames = Object.keys(dat[this.roomType])
     },
     roomName: function() {
       this.newGadget.Room_id = this.rooms[this.roomType][this.roomName]
     }
  },

  methods: {
    fetchGadgets: function () {
      this.$store.dispatch('room/fetchGadgets')
    },
    addGadget: function () {
      this.handleGadgetValue()
      .then(success => {
        if(success) {

        } else {
          alert("not pass valid")
        }
      })  
      this.show = false
      // this.$store.dispatch('room/postGadget', this.newGadget)
    },
    fetchRooms: function () {
      this.$store.dispatch('room/fetchRooms')
    },
    handleGadget: function() {
      this.newGadget.Name = this.gadgetName
      this.newGadget.Status = "Available"
      alert(Date().toString)
      
    },
    handleGadgetValue: async function() {
      // check form is valid

      //
      return false
    }
  },
  mounted() {
   this.fetchGadgets()
   this.fetchRooms()
  }
}
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

pad {
  position: relative;
  top: 100px;
}
</style>
