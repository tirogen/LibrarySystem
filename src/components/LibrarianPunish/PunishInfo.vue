<template>
    <b-container>
        <b-row class="py-md-2">
            <b-col>
                <b-form-input v-model="firstname" placeholder="Firstname"></b-form-input>
            </b-col>
            <b-col>
                <b-form-input v-model="lastname" placeholder="Lastname"></b-form-input>
            </b-col>
            <b-button class="fas fa-search" v-on:click="getPunishInfo">search</b-button>
        </b-row>
    </b-container>
</template>

<script>
import {mapState} from 'vuex'
export default {
  name: 'PunishInfo',
  props: {

  },
  data() {
    return {
      Firstname: "",
      Lastname: "",
      PunishInfo: "",
    }
  },
  methods: {
      getPunishInfo: function() {
          this.Pinfo = this.$store.dispatch("punish/getPunishInfo")
      }
  },
  computed: mapState({
    firstname: state => state.punish.firstname,
    lastname: state => state.punish.lastname,
    punishInfo: state => state.punish.punishInfo,

  }),
  mounted(){
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
