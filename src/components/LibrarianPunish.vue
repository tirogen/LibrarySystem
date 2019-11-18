<template>
  <div class="jumbotron bg-overlay">
    <h2>Library Punish</h2>
    <b-table :items="penalty" :fields="fields" striped responsive="sm">
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
import {mapState} from 'vuex'
export default {
  name: 'LibrarianPunish',
  props: {

  },
  data() {
    return {
      fields: ['Room', 'Name', 'Time In', 'Time Out', 'Manage'],
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
