<template>
    <b-container>
        <b-row class="py-md-2">
            <b-col>
                <b-form-input v-model="firstname" placeholder="Firstname"></b-form-input>
            </b-col>
            <b-col>
                <b-form-input v-model="lastname" placeholder="Lastname"></b-form-input>
            </b-col>
            <b-button v-on:click="getPunishInfo"><i class="fas fa-search"></i></b-button>
        </b-row>
        <b-row class="py-md-2">
        </b-row>
        <b-table :items="punishInfo" :fields="fields" striped responsive="sm">
          <template v-slot:cell(Manage)="row">
            <b-button size="sm" variant="danger" class="m-2">Pardon</b-button>
          </template>
        </b-table>
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
      firstname: '',
      lastname: '',
      fields: ['Penalty', 'Point','Date', 'Time', 'Manage'],
    }
  },
  methods: {
      getPunishInfo: function() {
          let data = {
                        'firstname': this.firstname,
                        'lastname': this.lastname
                      }
          this.punishinfo = this.$store.dispatch("punish/getPunishInfo", data);
      }
  },
  computed: mapState({
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
