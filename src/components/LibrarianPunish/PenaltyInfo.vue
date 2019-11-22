<template>
  <b-container>
    <b-table :items="penalties" :fields="fields" striped responsive="sm">
        <template v-slot:cell(Manage)="row">
            <b-button size="sm" @click="row.toggleDetails" class="mr-2">
            {{ row.detailsShowing ? 'Hide' : 'Show'}} Manage
            </b-button>
        </template>
        <template v-slot:row-details="row">
            <b-card>
            <b-button @click="setModal(row.item)" size="sm" variant="primary" class="m-2">Update</b-button>
            <b-button v-on:click="deletePenalty(row.item.id)" size="sm" variant="danger" class="m-2">Delete</b-button>
            </b-card>
        </template>
    </b-table>

    <!-- Update Modal -->
    <b-modal
      id="modal-penalty-update"
      ref="modal"
      title="Update penalty"
      @hidden="resetModal"
      @ok="handleOk()"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          label="Name"
        >
          <b-form-input
            id="name-input"
            v-model="selectedPenalty.Name"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group
          label="Point"
        >
          <b-form-input
            id="point-input"
            v-model="selectedPenalty.Point"
            required
          ></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
    <!--End of Update Modal -->
  </b-container>
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
      selectedPenalty: {
        "Name": '',
        "Point": '',
        "id": '',
      }
    }
  },
  methods: {
    deletePenalty: function(id){
      this.$store.dispatch('punish/deletePenalty', id);
    },

    //update Modal
    setModal(item) {
      this.selectedPenalty.id = item.id;
      this.selectedPenalty.Name = item.Name;
      this.selectedPenalty.Point = item.Point;
      this.$refs.modal.show();
    },
    resetModal() {
      this.selectedPenalty.Name = '';
      this.selectedPenalty.Point = '';
      this.selectedPenalty.id = '';
    },
    handleOk() {
      if (this.selectedPenalty.Name == '' || this.selectedPenalty.Point == '') {
        alert("Require name and point for penalty")
        return
      }
      if(this.selectedPenalty.Point != parseInt(this.selectedPenalty.Point, 10)){
        alert("Point have to be integer")
        return
      }
      this.$store.dispatch('punish/updatePenalty', this.selectedPenalty)
      this.$nextTick(() => this.$refs.modal.hide())
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
