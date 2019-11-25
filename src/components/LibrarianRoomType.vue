<template>
<div class="jumbotron bg-overlay">
  <h2>Room Types <b-button v-b-modal.modal-1 @click="addShow=true">ADD ROOM TYPES</b-button></h2>
  <div v-if="isLoading" class="w-100 my-5 d-flex align-items-center justify-content-center">
    <div class="pr-3"><i class="fas fa-circle-notch fa-spin fa-2x"></i></div>
    <div><strong style="font-size: 24px"> Loading... </strong></div>
  </div>
  <b-table v-else :items="roomTypes" :fields="fields" striped responsive="sm">
    <template v-slot:cell(Manage)="row">
      <b-button size="sm" @click="row.toggleDetails" class="mr-2">
        {{ row.detailsShowing ? 'Hide' : 'Show'}} Manage
      </b-button>
    </template>
    <template v-slot:row-details="row">
      <b-card>
        <ul>
          <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
        </ul>
      </b-card>
    </template>
    <template v-slot:row-details="row">
      <b-card>
        <b-button size="lg" variant="primary" class="m-2" @click="showModal(row.item.Type)">Update</b-button>
        <b-button size="lg" variant="danger" class="m-2" @click="showDeleteConfirm(row.item.Type)">Delete</b-button>
      </b-card>
    </template>
  </b-table>

  <b-modal v-model="show" title="Update Room Type">
    <b-container fluid class="bv-example-row bv-example-row-flex-cols">
      <b-row class="mb-1">
        <b-col sm="3">New Type</b-col>
        <b-col sm="9">
          <b-form-input id="current-input" v-model="Type"></b-form-input>
        </b-col>
      </b-row>
      <b-form-input id="range-2" v-model="Capacity" type="range" min="0" max="15" step="1"></b-form-input>
      <div class="mt-2">Capacity: {{Capacity}}</div>
    </b-container>
    <template v-slot:modal-footer>
      <b-button @click="show=false">Cancel</b-button>
      <b-button variant="primary" @click="update()">Update</b-button>
    </template>
  </b-modal>

  <b-modal v-model="addShow" title="ADD ROOM TYPES">
    <b-container fluid class="bv-example-row bv-example-row-flex-cols">
      <b-row class="mb-1">
        <b-col sm="3">Type</b-col>
        <b-col sm="9">
          <b-form-input id="current-input" v-model="Type"></b-form-input>
        </b-col>
      </b-row>
      <b-form-input id="range-2" v-model="Capacity" type="range" min="0" max="15" step="1"></b-form-input>
      <div class="mt-2">Capacity: {{Capacity}}</div>
    </b-container>
    <template v-slot:modal-footer>
      <b-button @click="addShow=false">Cancel</b-button>
      <b-button variant="primary" @click="addNew()">Add New</b-button>
    </template>
  </b-modal>

</div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: 'LibrarianRoomType',
  data() {
    return {
      fields: ["Type", "Capacity", "Manage"],
      OldType: null,
      Type: null,
      Capacity: null,
      show: false,
      addShow: false,
    }
  },
  methods: {
    resetInfoModal() {
      this.infoModal.title = "";
      this.infoModal.content = "";
    },
    showDeleteConfirm(type){
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
          if (value) {
            this.$store.dispatch('roomType/deleteRoomType', type)
          }
        })
    },
    showModal(type){
      this.Type = type
      this.OldType = type
      this.Capacity = 0
      this.show = true
    },
    update(){
      this.$store.dispatch('roomType/updateRoomType', {OldType: this.OldType, Type: this.Type, Capacity: this.Capacity})
      this.show = false
      this.Type = null
      this.OldType = null
      this.Capacity = 0
    },
    addNew(){
      this.$store.dispatch('roomType/addRoomType', {Type: this.Type, Capacity: this.Capacity})
      this.addShow = false
      this.Type = null
      this.OldType = null
      this.Capacity = 0
    }
  },
  computed: {
    ...mapState({
      isLoading: state => state.roomType.isLoading,
      roomTypes: state => state.roomType.roomTypes
    }),
  },
  mounted() {
    this.$store.dispatch('roomType/fetchRoomTypes')
  }
};
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
