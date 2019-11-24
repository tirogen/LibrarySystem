<template>
<div class="jumbotron bg-overlay">
  <h2>Room <b-button v-b-modal.modal-1 @click="addShow=true">ADD ROOM</b-button></h2>
  <div v-if="isLoading" class="w-100 my-5 d-flex align-items-center justify-content-center">
    <div class="pr-3"><i class="fas fa-circle-notch fa-spin fa-2x"></i></div>
    <div><strong style="font-size: 24px"> Loading... </strong></div>
  </div>
  <b-table v-else :items="rooms" :fields="fields" striped responsive="sm">
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
        <b-button size="lg" variant="primary" class="m-2" @click="showModal(row.item.id, row.item.Name)">Update</b-button>
        <b-button size="lg" variant="danger" class="m-2" @click="showDeleteConfirm(row.item.id)">Delete</b-button>
      </b-card>
    </template>
  </b-table>

  <b-modal v-model="show" title="Update Room">
    <b-container fluid class="bv-example-row bv-example-row-flex-cols">
      <b-row class="mb-1">
        <b-col sm="3">New Name</b-col>
        <b-col sm="9">
          <b-form-input id="current-input" v-model="Name"></b-form-input>
        </b-col>
      </b-row>
      <b-row class="mb-1">
        <b-col sm="3">Librarian</b-col>
        <b-col sm="9">
          <b-form-select v-model="Librarian" :options="newLibrarians" required></b-form-select>
        </b-col>
      </b-row>
      <b-row class="mb-1">
        <b-col sm="3">Room Type</b-col>
        <b-col sm="9">
          <b-form-select v-model="Type" :options="newRoomTypes" required></b-form-select>
        </b-col>
      </b-row>
    </b-container>
    <template v-slot:modal-footer>
      <b-button @click="show=false">Cancel</b-button>
      <b-button variant="primary" @click="update()">Update</b-button>
    </template>
  </b-modal>

  <b-modal v-model="addShow" title="ADD ROOM">
    <b-container fluid class="bv-example-row bv-example-row-flex-cols">
      <b-row class="mb-1">
        <b-col sm="3">Name</b-col>
        <b-col sm="9">
          <b-form-input id="current-input" v-model="Name"></b-form-input>
        </b-col>
      </b-row>
      <b-row class="mb-1">
        <b-col sm="3">Librarian</b-col>
        <b-col sm="9">
          <b-form-select v-model="Librarian" :options="newLibrarians" required></b-form-select>
        </b-col>
      </b-row>
      <b-row class="mb-1">
        <b-col sm="3">Room Type</b-col>
        <b-col sm="9">
          <b-form-select v-model="Type" :options="newRoomTypes" required></b-form-select>
        </b-col>
      </b-row>
    </b-container>
    <template v-slot:modal-footer>
      <b-button @click="addShow=false">Cancel</b-button>
      <b-button variant="primary" @click="addNew()">Add New</b-button>
    </template>
  </b-modal>

</div>
</template>

<script>
import {mapState} from "vuex";

export default {
  name: 'LibrarianRoom',
  data() {
    return {
      fields: ["Name", {key:'LibrarianName',label:'Librarian Name'}, "Type", "Manage"],
      id: null,
      Name: null,
      Type: null,

      show: false,
      addShow: false,
      Librarian: null
    }
  },
  methods: {
    resetInfoModal() {
      this.infoModal.title = "";
      this.infoModal.content = "";
    },
    showDeleteConfirm(id){
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
            this.$store.dispatch('roomManage/deleteRoom', id)
          }
        })
    },
    showModal(id, Name){
      this.id = id
      this.Name = Name
      this.show = true
    },
    update(){
      this.$store.dispatch('roomManage/updateRoom', {id: this.id, LibrarianUsername:this.Librarian, Name: this.Name, Type: this.Type})
      this.show = false
      this.id = null
      this.Name = null
      this.Librarian = null
      this.Type = null
    },
    addNew(){
      this.$store.dispatch('roomManage/addRoom', {LibrarianUsername: this.Librarian, Name: this.Name, Type: this.Type})
      this.addShow = false
      this.id = null
      this.Name = null
      this.Librarian = null
      this.Type = null
    }
  },
  computed: {
    ...mapState({
      isLoading: state => state.roomManage.isLoading,
      rooms: state => state.roomManage.rooms,
      librarians: state => state.roomManage.librarians,
      roomTypes: state => state.roomType.roomTypes
    }),
    newLibrarians() {
      return this.librarians.map((librarian)=>{
        return {value:librarian.Username , text:librarian.LibrarianName}
      })
    },
    newRoomTypes() {
      return this.roomTypes.map((roomType)=>{
        return {value:roomType.Type , text:roomType.Type}
      })
    },
  },
  mounted() {
    this.$store.dispatch('roomManage/fetchRooms')
    this.$store.dispatch('roomManage/fetchLibrarians')
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
