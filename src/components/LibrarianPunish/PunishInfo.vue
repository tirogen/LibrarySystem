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
        <b-row align-h="center" class="py-md-2">
          <b-col class="col-12">
            <b-card align="left" v-bind:title="punishInfo.fullName">
              <b-card-text>
                <b>Email: </b>{{punishInfo.email}}
              </b-card-text>
              <b-card-text>
                <b>Phone Number: </b>{{punishInfo.phoneNumber}}
              </b-card-text>
              <b-card-text>
                <b>Remaining Point: </b>{{punishInfo.remainingPoint}}
              </b-card-text>
              <b-dropdown id="dropdown-penalty" v-bind:text="selectedPenalty.Name" class="m-md-2">
                <b-dropdown-item 
                  v-for="penalty in penalties"
                  :key="penalty.id"
                  @click="selectedPenalty=penalty"
                  >
                  {{penalty.Name}}
                </b-dropdown-item>
              </b-dropdown>
              <b-button @click="punishStudent" size="sm" variant="danger" class="m-2">Punish</b-button>  
              <b-button @click="historyIsShow=!historyIsShow" size="sm" variant="primary" class="m-2">
                {{historyIsShow?"Hide History":"Show History"}}
              </b-button>   
            </b-card>
          </b-col>
        </b-row>
        <b-table :items="punishInfo.histories" :fields="fields" striped responsive="sm" v-if="historyIsShow">
          <template v-slot:cell(Manage)="row">
            <b-button @click="deletePunish(row.item.id)" size="sm" variant="primary" class="m-2">Pardon</b-button>
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
  components: {
  },
  data() {
    return {
      firstname: '',
      lastname: '',
      fields: ['Penalty', 'Point', 'Date', 'Time', 'Manage'],
      selectedPenalty: {Name: 'Select Penalty'},
      historyIsShow: false,
    }
  },
  methods: {
      getPunishInfo: function() {
          let data = {
            'firstname': this.firstname,
            'lastname': this.lastname
          }
          this.$store.dispatch("punish/getPunishInfo", data);
      },
      punishStudent: function() {
        let data = {
          'Penalty_id': this.selectedPenalty.id,
          'Date': '2019-11-19',
          'Time': '22:20:10',
          'Student_id': this.punishInfo.username,
          'Penalty': this.selectedPenalty.Name,
          'Point': this.selectedPenalty.Point
        }
        this.$store.dispatch("punish/punishStudent", data)
      },
      deletePunish: function(id) {
        this.$store.dispatch("punish/deletePunish", id)
      }
  },
  computed: mapState({
    punishInfo: state => state.punish.punishInfo,
    penalties: state => state.punish.penalties

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
