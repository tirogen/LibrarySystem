<template>
  <div class="jumbotron bg-overlay">
    <h2>Reserved Rooms</h2>
    <b-table :items="reservedRooms" :fields="fields" responsive="sm">
      <template v-slot:cell(TimeIn)="row">
        {{row.item.TimeIn == '00:00:00' ? '' : row.item.TimeIn}}
      </template>
      <template v-slot:cell(TimeOut)="row">
        {{row.item.TimeOut == '00:00:00' ? '' : row.item.TimeOut}}
      </template>
      <template v-slot:cell(Manage)="row">
        <b-button size="sm" @click="row.toggleDetails" class="mr-2">
          {{ row.detailsShowing ? 'Hide' : 'Show'}} Manage
        </b-button>
      </template>
      <template v-slot:row-details="row">
        <b-card>
          <b-button v-if="row.item.TimeIn == '00:00:00'" size="sm" variant="primary" class="m-2" @click="CheckIn(row.item.id)">Check in</b-button>
          <b-button v-else-if="row.item.TimeOut == '00:00:00'" size="sm" variant="success" class="m-2" @click="CheckOut(row.item.id)">Check out</b-button>
          <b-button v-else disabled size="sm" class="m-2">Disabled</b-button>
          <b-button v-if="row.item.TimeIn == '00:00:00'" size="sm" variant="danger" class="m-2" @click="showDeleteConfirm(row.item.RoomTime_id)">Delete</b-button>
          <b-button v-else disabled size="sm" variant="danger" class="m-2">Delete</b-button>
        </b-card>
      </template>
    </b-table>
    <b-button block variant="primary">See all</b-button>
  </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: 'LibrarianReserved',
  props: {

  },
  data() {
    return {
      fields: ['Room', 'Name', {key:'StartTime',label:'Start Time'}, {key:'EndTime',label:'End Time'}, {key:'TimeIn',label:'Time In'}, {key:'TimeOut',label:'Time Out'}, 'Date', 'Manage'],
    }
  },
  methods: {
    CheckIn(id) {
      this.$store.dispatch('librarian/checkInReservedRoom', id)
    },
    CheckOut(id) {
      this.$store.dispatch('librarian/checkOutReservedRoom', id)
    },
    showDeleteConfirm(id) {
        this.$bvModal.msgBoxConfirm('Please confirm that you want to delete.', {
          title: 'Please Confirm',
          size: 'sm',
          buttonSize: 'sm',
          okVariant: 'danger',
          okTitle: 'YES',
          cancelTitle: 'NO',
          footerClass: 'p-2',
          hideHeaderClose: false,
          centered: true
        })
        .then(value => {
            if(value){
                this.$store.dispatch('librarian/deleteReservedRoom', id)
            }
        })
    }
  },
  computed: mapState({
    reservedRooms: state => state.librarian.reservedRooms
  }),
  mounted(){
    this.$store.dispatch('librarian/getReservedRooms')
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
