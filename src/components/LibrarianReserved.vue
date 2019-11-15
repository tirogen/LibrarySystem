<template>
  <div>
    <b-table :items="items" :fields="fields" striped responsive="sm">
      <template v-slot:cell(show_details)="row">
        <b-button size="sm" @click="row.toggleDetails" class="mr-2">
          {{ row.detailsShowing ? 'Hide' : 'Show'}} Details
        </b-button>
      </template>

      <template v-slot:row-details="row">
        <b-card>
          <b-row class="mb-2">
            <b-col sm="3" class="text-sm-right"><b>Room name:</b></b-col>
            <b-col>{{ row.item['Room name'] }}</b-col>
          </b-row>

          <b-row class="mb-2">
            <b-col sm="3" class="text-sm-right"><b>Reserver:</b></b-col>
            <b-col>{{ row.item.Reserver }}</b-col>
          </b-row>

          <b-button size="sm" @click="row.toggleDetails">Hide Details</b-button>
        </b-card>
      </template>
    </b-table>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'LibrarianReserved',
  props: {

  },
  data() {
    return {
      fields: ['Room name', 'Reserver', 'Start time', 'Duration', 'show_details'],
      items: [
        {'Room name': 'Semina Room 6', 'Reserver': 'Nithi Tunti', 'Start time': '10:30' , 'Duration': '2 hrs'},
      ]
    }
  },
  computed: mapState({
    reservedRooms: state => state.reservedRooms
  }),
  created(){
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
