<template>
<div class="jumbotron bg-overlay">
  <h2>Room Types</h2>
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
        <b-button size="lg" variant="primary" class="m-2" @click="Update(row.item.Type)">Update</b-button>
        <b-button size="lg" variant="danger" class="m-2">Delete</b-button>
      </b-card>
    </template>
  </b-table>

  <b-button v-b-modal.modal-prevent-closing>Open Modal</b-button>
  <b-modal
    id="modal-prevent-closing"
    ref="modal"
    title="Update Room Type"
    @show="resetModal"
    @hidden="resetModal"
    @ok="handleOk"
  >
  <b-container fluid class="bv-example-row bv-example-row-flex-cols">
    <b-row class="mb-1">
      <b-col cols="1.5" class>Current type</b-col>
      <b-col>
        <b-form-input id="current-input" v-model="OldType" disabled></b-form-input>
      </b-col>
    </b-row>
  </b-container>

  </b-modal>
</div>
</template>

<script>
import {
  mapState
} from 'vuex'

export default {
  name: 'LibrarianRoomType',
  data() {
    return {
      fields: ["Type", "Capacity", "Manage"],
      OldType: null,
      Type: null,
      Capacity: null
    }
  },
  methods: {
    resetInfoModal() {
      this.infoModal.title = ''
      this.infoModal.content = ''
    },
    showDeleteConfirm(type) {
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
            this.$store.dispatch('roomType/deleteRoomTypes', type)
          }
        })
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
