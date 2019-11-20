<template>
  <div class="jumbotron bg-overlay">
    <h2>Punishment</h2>
    <b-tabs>
      <b-tab title="Penalty Type">
      <PenaltyInfo></PenaltyInfo>
      </b-tab>
      <b-tab title="Punish Menu">
      <PunishInfo></PunishInfo>
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import PunishInfo from './PunishInfo.vue'
import PenaltyInfo from './PenaltyInfo.vue'
export default {
  name: 'LibrarianPunish',
  props: {

  },
  components: {
    PunishInfo,
    PenaltyInfo,
  },
  data() {
    return {
      fields: ['id', 'Name', 'Point', 'Manage'],
    }
  },
  methods: {
    deletePenalty: function(id){
      this.$store.dispatch('punish/deletePenalty', id)
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
