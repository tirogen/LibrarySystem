<template>
  <div class="jumbotron bg-overlay">
    <h2>
      Punishment
      <b-button  v-b-modal.modal-add-penalty>ADD PENALTY</b-button>
    </h2>
    <b-tabs>
      <b-tab title="Penalty Type">
      <PenaltyInfo></PenaltyInfo>
      </b-tab>
      <b-tab title="Punish Menu">
      <PunishInfo></PunishInfo>
      </b-tab>
    </b-tabs>

     <!-- Add Penalty Modal -->
    <b-modal
      id="modal-add-penalty"
      ref="modal"
      title="Add Penalty"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk()"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          label="Name"
        >
          <b-form-input
            id="name-input"
            v-model="penalty.Name"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group
          label="Point"
        >
          <b-form-input
            id="point-input"
            v-model="penalty.Point"
            required
          ></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
    <!--End of Add Penalty Modal -->
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
      penalty: {
        'Name': '',
        'Point': '',
      }

    }
  },
  methods: {
    deletePenalty: function(id){
      this.$store.dispatch('punish/deletePenalty', id)
    },
    //add Modal
    resetModal() {
      this.penalty.Name = '';
      this.penalty.Point = '';
    },
    handleOk() {
      if (this.penalty.Name == '' || this.penalty.Point == '') {
        alert("Require name and point for penalty")
        return
      }
      if(this.penalty.Point != parseInt(this.penalty.Point, 10)){
        alert("Point have to be integer")
        return
      }
      this.$store.dispatch('punish/addPenalty', this.penalty)
      this.$nextTick(() => this.$refs.modal.hide())
    }
    //end of add modal
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
