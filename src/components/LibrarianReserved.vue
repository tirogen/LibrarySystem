<template>
  <div class="jumbotron bg-overlay">
    <h2>Reserved Rooms</h2>
    <b-table :items="reservedRooms" :fields="fields" striped responsive="sm">
      <template v-slot:cell(Manage)="row">
        <b-button size="sm" @click="row.toggleDetails" class="mr-2">
          {{ row.detailsShowing ? 'Hide' : 'Show'}} Manage
        </b-button>
      </template>
      <template v-slot:row-details="row">
        <b-card>
          <b-button size="sm" variant="primary" class="m-2">Check in</b-button>
          <b-button size="sm" variant="danger" class="m-2" @click="showDeleteConfirm(row.item.id)">Delete</b-button>
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
      fields: ['Room', 'Name', 'Start Time', 'End Time', 'Time In', 'Time Out', 'Date', 'Manage'],
    }
  },
  methods: {
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
                this.$store.dispatch('librarian/deleteReservedRooms', id)
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
