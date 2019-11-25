<template>
  <div class="jumbotron bg-overlay">
    <h2>
      Borrow Book
      <b-button v-b-modal.modal-borrow @click="showGadgetModal()">ADD BORROWING BOOK</b-button>
    </h2>
    <!-- Add Borrow Modal -->
    <div>
      <b-modal id="modal-borrow" v-model="show" title="ADD BORROWING BOOK">
        <b-container fluid class="bv-example-row bv-example-row-flex-cols">
          <b-row class="mb-1 text-center" align-v="start">
            <b-col cols="1.7"></b-col>
            <b-col>RoomType</b-col>
            <b-col>RoomName</b-col>
          </b-row>
          <b-row class="mb-1">
            <b-col cols="1.5" class>Gadget Name</b-col>
            <b-col>
              <b-form-input id="name-input" v-model="gadgetName" required></b-form-input>
            </b-col>
          </b-row>
          <b-row v-if="this.action=='UPDATE'">
            <b-col cols="1.5" class>Available Status</b-col>
            <b-col>
              <b-form-select v-model="available" :options="statuses"></b-form-select>
            </b-col>
          </b-row>
          <b-row class="mb-1">
            <b-col cols="4.5" class>Purchase Date</b-col>
            <b-col class="text-center">
              <datepicker
                :format="customFormatter"
                v-model="cal.date"
                :language="th"
                :disabled-dates="cal.disabledDates"
                name="uniquename"
              ></datepicker>
            </b-col>
          </b-row>
          <b-row align-h="start">
            <b-col>CLICK BOX TO CHANGE PURCHASE DATE</b-col>
          </b-row>
        </b-container>
        <template v-slot:modal-footer>
          <div class="w-100">
            <!-- <p class="float-left">Submit to add gadget</p> -->
            <b-button variant="primary" size="sm" class="float" @click="checkAction()">CONFIRM</b-button>
            <b-button variant="primary" size="sm" class="float-right" @click="show=false">CANCEL</b-button>
          </div>
        </template>
      </b-modal>
    </div>
    <!-- End of add Borrow modal -->
    <!-- FILTER FEATURE -->

    <b-row>
      <b-col lg="6" class="my-1">
        <b-form-group
          label="Filter"
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          label-for="filterInput"
          class="mb-0"
        >
          <b-input-group size="sm">
            <b-form-input
              v-model="filter"
              type="search"
              id="filterInput"
              placeholder="Type to Search"
            ></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>
          </b-input-group>
          <b-input-group size="sm" v-if="false">
            <b-form-select v-model="filter" size="sm" :options="filterOption"></b-form-select>
          </b-input-group>
        </b-form-group>
      </b-col>

      <b-col lg="6" class="my-1">
      </b-col>

      <b-col sm="5" md="6" class="my-1">
        <b-form-group
          label="Per page"
          label-cols-sm="6"
          label-cols-md="4"
          label-cols-lg="3"
          label-align-sm="right"
          label-size="sm"
          label-for="perPageSelect"
          class="mb-0"
        >
          <b-form-select v-model="perPage" id="perPageSelect" size="sm" :options="pageOptions"></b-form-select>
        </b-form-group>
      </b-col>

      <b-col sm="7" md="6" class="my-1">
        <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          align="fill"
          size="sm"
          class="my-0"
        ></b-pagination>
      </b-col>
    </b-row>

    <div v-if="isLoading" class="w-100 my-5 d-flex align-items-center justify-content-center">
      <div class="pr-3">
        <i class="fas fa-circle-notch fa-spin fa-2x"></i>
      </div>
      <div>
        <strong style="font-size: 24px">Loading...</strong>
      </div>
    </div>

    <!-- End of Filter form -->
    <b-table
      :items="borrow"
      :fields="fields"
      striped
      responsive="sm"
      :current-page="currentPage"
      :per-page="perPage"
      :filter="filter"
      :filterIncludedFields="filterOn"
      :sort-by.sync="sortBy"
      :sort-desc.sync="sortDesc"
      :sort-direction="sortDirection"
      id="table-transition-example"
    >
      <template v-slot:cell(Manage)="row">
        <b-button
          size="sm"
          @click="row.toggleDetails"
          class="mr-2"
        >{{ row.detailsShowing ? 'Hide' : 'Show'}} Manage</b-button>
      </template>
      <template v-slot:row-details="row">
        <b-card>
          <b-button
            size="sm"
            variant="danger"
            class="m-2"
            @click="showDeleteConfirm(row.item)"
          >Delete</b-button>
        </b-card>
      </template>
    </b-table>
  </div>
</template>

<script>
import { mapState } from "vuex";
import Datepicker from "vuejs-datepicker";
import { en, th } from "vuejs-datepicker/dist/locale";

export default {
  name: "Borrow",
  props: {},
  data() {
    return {
      statuses: ["Available", "NotAvailable"],
      action: "ADD",
      en: en,
      th: th,
      cal: {
        date: new Date(),
        disabledDates: {
         to: new Date()
        }
      },
      bookName: "",
      fields: [
        { key: "bookISBN", sortable: true },
        { key: "bookname", sortable: true },
        { key: "studentName", sortable: true },
        "Manage"
      ],
      show: false,
      roomName: "",
      roomType: "",
      nameOption: "",
      currentPage: 1,
      perPage: 5,
      pageOptions: [1, 5, 10, 15],
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      filter: null,
      filterOn: [],
      transProps: {
        // Transition name
        name: "flip-list"
      },
      filterOption: [],
      allRoomNames: [],
      IsTypeToSearch: true
    };
  },
  computed: {
    ...mapState({
      isLoading: state => state.borrow.isLoading,
      isSuccess: state => state.borrow.isSuccess,
      isError: state => state.borrow.isError,
      borrow: state => {
        // alert("vuex gadget update")
        return state.borrow;
      },
      borrow: state => state.borrow,
      book: state => Object.keys(state.book.book.ISBN),
      username: state => state.username,
      totalRows: state => state.borrow.length
    }),
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter(f => f.sortable)
        .map(f => {
          return {
            text: f.label,
            value: f.key
          };
        });
    }
  },
  watch: {
    book: function() {
      if (this.action == "ADD") {
        this.$store.dispatch("book/fetchbooks", this.book);
      } else if (this.action == "UPDATE" && this.book != "") {
        // check roomType in key
        // this.rooms[]
        // if (this.roomName == "") {
        this.$store.dispatch("book/fetchbooks", this.book);
        // }
      }
      //  this.roomNames = Object.keys(dat[this.roomType])
    }
  },

  methods: {
    customFormatter(date) {
      let mo = date.getMonth() + 1;
      if (mo <= 9) {
        var m = "0" + mo;
      } else {
        m = mo;
      }
      let dd = date.getDate();
      if (dd <= 9) {
        var d = "0" + dd;
      } else {
        d = dd;
      }
      let dateFormat = date.getFullYear() + "-" + m + "-" + d;
      this.newBorrow.EndDate = dateFormat;
      return dateFormat;
    },
    fetchBorrow: function(){
      this.$store.dispatch("borrow/fetchBorrow");
    },
    deleteBorrow: function(id) {
      // get data
      this.$store.dispatch("borrow/deleteBorrow", id);
    },
    showDeleteConfirm(item) {
      this.$bvModal
        .msgBoxConfirm("Please confirm that you want to delete.", {
          title: "PleasConfirm",
          size: "sm",
          buttonSize: "sm",
          okVariant: "danger",
          okTitle: "YES",
          cancelTitle: "NO",
          footerClass: "p-2",
          hideHeaderClose: false,
          centered: true
        })
        .then(value => {
          if (value) {
            // alert(Object.keys(item))

            this.deletedBorrow(item.ID);
          } else {
            // asdasda
          }
        });
    }
  },
  mounted() {
    this.fetchBorrow()
  },
  components: {
    Datepicker
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
/* .colBackground{
    background-color: lightseagreen;
} */

table#table-transition-example .flip-list-move {
  transition: transform 1s;
}
</style>
