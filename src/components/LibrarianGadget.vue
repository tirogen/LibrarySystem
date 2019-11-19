<template>
  <div class="jumbotron bg-overlay">
    <h2>Gadget
    <b-button v-b-modal.modal-1>ADD GADGET</b-button>
    </h2>
    <!-- Add GadGet Modal -->
    <b-modal id="modal-1" title="BootstrapVue">
        <div class="modal-content">
            <div class="modal-body">
                  <label for="GadgetName">Gadget Name</label>
                  <input
                    type="text"
                    class="form-control"
                    id="GadgetName"
                    placeholder="Enter Gadget Name"
                    v-model="newGadget.GadgetName"
                    required="required" >
            </div>
        </div>
      <template v-slot:modal-footer="{ ok, cancel }">
        <b>Custom Footer</b>
        <!-- Emulate built in modal footer ok and cancel button actions -->
        <b-button size="sm" variant="success" v-on:click="addGadget()">
          OK
        </b-button>
        <b-button size="sm" variant="danger" @click="cancel()">
          Cancel
        </b-button>
      </template>
    </b-modal>
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
import { mapState } from 'vuex';
export default {
  name: 'Gadget',
  props: {

  },
  data() {
    return {
      fields: ['GadgetName', 'Status', 'PurchasedDate', 'RoomName', 'Manage'],
      newGadget: { 'Name': null, 'Status': null, 'PurchasedDate': null, 'Room_id': null}
    }
  },
  mounted() {
   this.fetchGadgets()
   this.fetchRooms()
  },
  computed: mapState({
    isLoading: state => state.room.isLoading,
    isSuccess: state => state.room.isSuccess,
    isError: state => state.room.isError,
    gadgets: state => {
      return state.room.gadgets
    },
    rooms: state => {
      return state.room.rooms
    }
  }),

  methods: {
    fetchGadgets: function(){
        this.$store.dispatch('room/fetchGadgets')
    },
    addGadget: function(){
      this.$store.dispatch('room/postGadget', this.newGadget)
    },
    fetchRooms: function() {
      this.$store.dispatch('room/fetchRooms')
    }
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
</style>
