<template>
  <div class="jumbotron bg-overlay">
    <h2>Punishment</h2>
    <b-table :items="penalties" :fields="fields" striped responsive="sm">
      <template v-slot:cell(Manage)="row">
        <b-button size="sm" @click="row.toggleDetails" class="mr-2">
          {{ row.detailsShowing ? 'Hide' : 'Show'}} Manage
        </b-button>
      </template>
      <template v-slot:row-details="row">
        <b-card>
          <b-button size="sm" variant="primary" class="m-2">Edit</b-button>
          <b-button v-on:click="deletePenalty" size="sm" variant="danger" class="m-2">Delete</b-button>
        </b-card>
      </template>
    </b-table>
    <b-button block variant="primary">See all</b-button>
    <PunishInfo></PunishInfo>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import PunishInfo from './PunishInfo.vue'
export default {
  name: 'LibrarianPunish',
  props: {

  },
  components: {
    PunishInfo
  },
  data() {
    return {
      fields: ['id', 'Name', 'Point', 'Manage'],
    }
  },
  methods: {
    deletePenalty: function(event){
      // this.$store.dispatch('punish/DeletePenalty/')
    }
  },
  computed: mapState({
    penalties: state => state.punish.penalties
  }),
  mounted(){
    this.$store.dispatch('punish/getAllPenalties')
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
