<template>
  <div class="jumbotron bg-overlay">
    <h2>
      Borrow Book
      <b-button v-b-modal.modal-borrow @click="showBorrowModal()">ADD BORROWING BOOK</b-button>
    </h2>
    <!-- Add Borrow Modal -->
    <div>
      <b-modal id="modal-borrow" v-model="show" title="ADD BORROWING BOOK">
        <b-container fluid class="bv-example-row bv-example-row-flex-cols">
          <b-row class="mb-1">
            <b-col cols="1.5" class>Username</b-col>
            <b-col>
              <b-form-select id="name-input" :options="studentList" v-model="username" required></b-form-select>
            </b-col>
          </b-row>

          <b-row class="mb-1">
            <b-col cols="1.5" class>Book_ISBN</b-col>
            <b-col>
              <b-form-input id="name-input" v-model="bookisbn" required></b-form-input>
            </b-col>
          </b-row>

          <b-row class="mb-1">
            <b-col cols="1.5" class>Book_ID</b-col>
            <b-col>
              <b-form-select
                id="name-input"
                :disabled="disableBookid"
                v-model="bookid"
                :options="availableIDList"
                required
              ></b-form-select>
            </b-col>
          </b-row>

          <b-row class="mb-1">
            <b-col cols="4.5" class>EndDate</b-col>
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
            <b-col>CLICK BOX TO CHANGE END DATE</b-col>
          </b-row>
        </b-container>
        <template v-slot:modal-footer>
          <div class="w-100">
            <!-- <p class="float-left">Submit to add gadget</p> -->
            <b-button variant="primary" size="sm" class="float" @click="addBorrow()">OK</b-button>
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

      <b-col lg="6" class="my-1"></b-col>

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
      v-else
      show-empty
      :items="borrows"
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
      isISBNvalid: false,
      username: "",
      bookisbn: "",
      bookid: 0,
      disableBookid: false,
      endDate: "",
      obj: {
        startDate: "",
        endDate: "",
        bookID: "",
        studentID: ""
      },
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
        "bookID",
        { key: "bookISBN", sortable: true },
        { key: "bookName", sortable: true },
        { key: "studentID", sortable: true },
        { key: "endDate", sortable: false },
        "Manage"
      ],
      show: false,
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
      IsTypeToSearch: true,
      option: "enddate"
    };
  },
  computed: {
    ...mapState({
      isLoading: state => state.borrow.isLoading,
      isSuccess: state => state.borrow.isSuccess,
      isError: state => state.borrow.isError,
      borrows: state => {
        return state.borrow.borrows;
      },
      totalRows: state => state.borrow.borrows.length,
      isbnList: state => state.book.isbns,
      bookdict: state => state.book.bookdict,
      studentList: state => state.student.studentList,
      studentScore: state => state.borrow.studentScore
    }),
    availableIDList: function() {
      if (this.bookdict == {} || this.isISBNvalid == false) {
        return [];
      }
      const bookdict = this.bookdict;
      const bookisbn = this.bookisbn;
      const obj = bookdict[bookisbn];
      const arr = obj["number"].filter(num => {
        const index = bookdict[bookisbn]["number"].findIndex(mem => mem == num);
        return bookdict[bookisbn]["status"][index] == "Available";
      });
      // console.log(arr);
      return arr;
    },
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
    bookisbn: function() {
      this.isISBNvalid = this.isbnList.includes(this.bookisbn);
      if (this.isISBNvalid) {
        this.disableBookid = false;
      } else {
        this.disableBookid = true;
      }
    },
    username: function() {
      if(this.studentList.includes(this.username)) {
        this.$store.dispatch("borrow/fetchStudentPoint", this.username);
      }
    },
    studentScore: function() {
      // console.log(this.studentScore[0]);
      if (this.studentScore[0]["Student_id"] === this.username) {
        //alert("check student score");
        if (this.studentScore[0]["TotalPoint"] <= 0) {
          alert("borrow restricted for this misbehaved student");
          this.username = "";
        } else {
          //alert("no blacklist")
        }
      }
    }
    // ,
    // bookdict: function() {
    //   alert("2")
    // }
  },

  methods: {
    addBorrow() {
      // already set endDate
      this.option = "startdate";
      this.obj.startDate = this.customFormatter(new Date());
      this.option = "enddate";
      this.obj.bookID = this.bookid;
      this.obj.studentID = this.username;
      this.obj.endDate = this.endDate;
      this.$store.dispatch("borrow/postBorrow", this.obj);
      this.show = false;
    },
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
      if (this.option == "enddate") {
        this.endDate = dateFormat;
      }
      return dateFormat;
    },
    fetchBorrow: function() {
      this.$store.dispatch("borrow/fetchBorrow");
    },
    deleteBorrow: function(id) {
      // get data
      this.$store.dispatch("borrow/deleteBorrow", id);
    },
    showBorrowModal: function() {
      // show and what are u gonna do
      // console.log("ss");
      this.$store.dispatch('book/fetchBooks')
      this.username = ""
      this.bookisbn = ""
      this.bookid = ""
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
            // alert("delete");
            this.deleteBorrow(item.borrowID);
          } else {
            // asdasda
          }
        });
    }
  },
  mounted() {
    this.fetchBorrow();
    // this.$store.dispatch("borrow/fetchStudentPoint");
    this.$store.dispatch("student/fetchStudentList");
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
