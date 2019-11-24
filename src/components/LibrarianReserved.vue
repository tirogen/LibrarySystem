<template>
<div class="jumbotron bg-overlay">
  <h2>Reserved Rooms</h2>
  <b-container fluid>
    <b-row>
      <b-col lg="6" class="my-1">
        <b-form-group label="Filter" label-cols-sm="3" label-align-sm="right" label-size="sm" label-for="filterInput" class="mb-0">
          <b-input-group size="sm">
            <b-form-input v-model="filter" type="search" id="filterInput" placeholder="Type to Search"></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>
      </b-col>

      <b-col lg="6" class="my-1">
        <b-form-group label="Filter On" label-cols-sm="3" label-align-sm="right" label-size="sm" description="Leave all unchecked to filter on all data" class="mb-0">
          <b-form-checkbox-group v-model="filterOn" class="mt-1">
            <b-form-checkbox value="Room">Room</b-form-checkbox>
            <b-form-checkbox value="Name">Name</b-form-checkbox>
            <b-form-checkbox value="StartTime">Start Time</b-form-checkbox>
            <b-form-checkbox value="EndTime">End Time</b-form-checkbox>
            <b-form-checkbox value="TimeIn">Time In</b-form-checkbox>
            <b-form-checkbox value="TimeOut">Time Out</b-form-checkbox>
            <b-form-checkbox value="Date">Date</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
      </b-col>

      <b-col sm="5" md="6" class="my-1">
        <b-form-group label="Per page" label-cols-sm="6" label-cols-md="4" label-cols-lg="3" label-align-sm="right" label-size="sm" label-for="perPageSelect" class="mb-0">
          <b-form-select v-model="perPage" id="perPageSelect" size="sm" :options="pageOptions"></b-form-select>
        </b-form-group>
      </b-col>

      <b-col sm="7" md="6" class="my-1">
        <b-pagination v-model="currentPage" :total-rows="totalRows" :per-page="perPage" align="fill" size="sm" class="my-0"></b-pagination>
      </b-col>
    </b-row>
    <div v-if="isLoading" class="w-100 my-5 d-flex align-items-center justify-content-center">
      <div class="pr-3"><i class="fas fa-circle-notch fa-spin fa-2x"></i></div>
      <div><strong style="font-size: 24px"> Loading... </strong></div>
    </div>
    <b-table v-else show-empty small stacked="md" :items="reservedRooms" :fields="fields" :current-page="currentPage" :per-page="perPage" :filter="filter" :filterIncludedFields="filterOn" :sort-by.sync="sortBy" :sort-desc.sync="sortDesc"
      :sort-direction="sortDirection" @filtered="onFiltered">
      <template v-slot:cell(TimeIn)="row">
        {{row.item.TimeIn == '00:00:00' ? '' : row.item.TimeIn}}
      </template>
      <template v-slot:cell(TimeOut)="row">
        {{row.item.TimeOut == '00:00:00' ? '' : row.item.TimeOut}}
      </template>

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
          <b-button v-if="row.item.TimeIn == '00:00:00'" size="lg" variant="primary" class="m-2" @click="CheckIn(row.item.id)">Check in</b-button>
          <b-button v-else-if="row.item.TimeOut == '00:00:00'" size="lg" variant="success" class="m-2" @click="CheckOut(row.item.id)">Check out</b-button>
          <b-button v-else disabled size="lg" class="m-2">Disabled</b-button>
          <b-button v-if="row.item.TimeIn == '00:00:00'" size="lg" variant="danger" class="m-2" @click="showDeleteConfirm(row.item.RoomTime_id)">Delete</b-button>
          <b-button v-else disabled size="lg" variant="danger" class="m-2">Delete</b-button>
        </b-card>
      </template>
    </b-table>
  </b-container>
</div>
</template>

<script>
import {
  mapState
} from 'vuex'

export default {
  name: 'LibrarianReserved',
  props: {

  },
  data() {
    return {
      fields: [{
        key: 'Room',
        sortable: true
      }, {
        key: 'Name',
        sortable: true
      }, {
        key: 'StartTime',
        label: 'Start Time',
        sortable: true
      }, {
        key: 'EndTime',
        label: 'End Time',
        sortable: true
      }, {
        key: 'TimeIn',
        label: 'Time In',
        sortable: true
      }, {
        key: 'TimeOut',
        label: 'Time Out',
        sortable: true
      }, {
        key: 'Date',
        sortable: true
      }, 'Manage'],
      currentPage: 1,
      perPage: 5,
      pageOptions: [1, 5, 10, 15],
      sortBy: '',
      sortDesc: false,
      sortDirection: 'asc',
      filter: null,
      filterOn: [],
    }
  },
  methods: {
    resetInfoModal() {
      this.infoModal.title = ''
      this.infoModal.content = ''
    },
    onFiltered(filteredItems) {
      totalRows = filteredItems.length
      this.currentPage = 1
    },
    CheckIn(id) {
      this.$store.dispatch('librarian/checkInReservedRoom', id)
    },
    CheckOut(id) {
      this.$store.dispatch('librarian/checkOutReservedRoom', id)
    },
    showDeleteConfirm(id) {
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
            this.$store.dispatch('librarian/deleteReservedRoom', id)
          }
        })
    }
  },
  computed: {
    ...mapState({
      isLoading: state => state.librarian.isLoading,
      reservedRooms: state => state.librarian.reservedRooms,
      totalRows: state => state.librarian.reservedRooms.length
    }),
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter(f => f.sortable)
        .map(f => {
          return {
            text: f.label,
            value: f.key
          }
        })
    }
  },
  mounted() {
    this.$store.dispatch('librarian/getReservedRooms')
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
