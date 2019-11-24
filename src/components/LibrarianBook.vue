<template>
  <div class="jumbotron bg-overlay">
    <h2>
      Book
      <b-button v-b-modal.modal-add-book @click="fillData()">ADD BOOK</b-button>
    </h2>
    <!-- Add Book Modal -->
    <b-modal v-model="showAddModal" id="modal-add-book" title="ADD BOOK">
      <div class="modal-content">
        <div class="modal-body">
          <b-card bg-variant="light">
            <b-form-group
              id="fieldset-1"
              description="Let us know your name."
              label="ENTER Book ISBN"
              label-size="lg"
              label-for="input-1"
              label-class="font-weight-bold pt-0"
            >
              <b-form-input id="input-1" v-model="bookFillInfo.dat.isbn" trim></b-form-input>
            </b-form-group>

            <b-form-group
              id="fieldset-horizontal"
              label="ENTER Book Info"
              label-size="lg"
              label-align-sm="left"
              label-class="font-weight-bold pt-0"
              description="Let us know your ISBN."
              label-for="input-horizontal"
              class="mb-0"
            >
              <b-form-group
                label-cols-sm="3"
                label="Book Name:"
                label-align-sm="right"
                label-for="nested-bookName"
              >
                <b-form-input
                  :disabled="isBookInfoRestrict"
                  v-model="bookFillInfo.dat.name"
                  id="nested-bookName"
                ></b-form-input>
              </b-form-group>
              <b-form-group
                label-cols-sm="3"
                label="Category:"
                label-align-sm="right"
                label-for="nested-category"
              >
                <b-form-input
                  :disabled="isBookInfoRestrict"
                  v-model="bookFillInfo.dat.category"
                  id="nested-category"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                label-cols-sm="3"
                label="Author:"
                label-align-sm="right"
                label-for="nested-author"
              >
                <b-form-input
                  :disabled="isBookInfoRestrict"
                  v-model="bookFillInfo.dat.author"
                  id="nested-author"
                ></b-form-input>
              </b-form-group>
            </b-form-group>
          </b-card>
        </div>
      </div>
      <template v-slot:modal-footer="{ ok, cancel }">
        <b>IF YOU COOL, PRESS HERE</b>
        <!-- Emulate built in modal footer ok and cancel button actions -->
        <b-button size="sm" variant="success" v-on:click="addBook(isBookInfoRestrict)">OK</b-button>
        <b-button size="sm" variant="danger" @click="cancel()">Cancel</b-button>
      </template>
    </b-modal>
    <!-- End of add Book modal -->
    <!-- Start delete Modal -->
    <b-modal id="modal-delete-book" title="DELETE BOOK" v-model="showDeleteModal" hide-footer>
      <b-jumbotron>
        <template v-slot:header>Condition</template>

        <template v-slot:lead>You will be not able to redo this action.</template>

        <hr class="my-4" />

        <p>Need to choose fill BOOK ID To delete</p>
        <div>
          <b-form-select v-model="deletedID" :options="deletedIDOption" class="mb-3"></b-form-select>
        </div>
      </b-jumbotron>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" @click="show=false">CLOSE</button>
        <button
          type="button"
          class="btn btn-danger"
          @click="showDeleteConfirm(deletedID)"
          data-dismiss="modal"
        >OK</button>
      </div>
    </b-modal>
    <!-- End of delete Modal  -->

    <!-- FILTER FEATURE -->

    <b-row>
      <b-col lg="6" class="my-1">
        <b-form-group
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          label-for="sortBySelect"
          class="mb-0"
        ></b-form-group>
      </b-col>

      <b-col lg="6" class="my-1">
        <b-form-group
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          label-for="initialSortSelect"
          class="mb-0"
        ></b-form-group>
      </b-col>

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
        <b-form-group
          label="Filter On"
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          description="Leave all unchecked to filter on all data"
          class="mb-0"
        >
          <b-form-checkbox-group v-model="filterOn" class="mt-1">
            <b-form-checkbox value="isbn">ISBN</b-form-checkbox>
            <b-form-checkbox value="name">BookName</b-form-checkbox>
            <b-form-checkbox value="category">Category</b-form-checkbox>
            <b-form-checkbox value="author">Author</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
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
      :items="books"
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
          <!-- <b-button size="sm" variant="primary" class="m-2">Check in</b-button> -->
          <b-button
            size="lg"
            variant="primary"
            class="m-2"
            v-b-modal.modal-delete-book
            @click="loadRowData(row.item, 'ADD MORE')"
          >ADD MORE</b-button>
          <b-button
            size="lg"
            variant="danger"
            class="m-2"
            v-b-modal.modal-delete-book
            @click="loadRowData(row.item,'DELETE')"
          >Delete</b-button>
        </b-card>
      </template>
    </b-table>
    <b-button block variant="primary">See all</b-button>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "Book",
  props: {},
  data() {
    return {
      fields: [
        { key: "isbn", label: "ISBN", sortable: true },
        { key: "name", label: "BookName", sortable: true},
        { key: "category", label: "Category", sortable:true },
        { key: "author", label: "Author",sortable:true },
        { key: "num", label: "Count",sortable:true },
        "Manage"
      ],
      isInStock: false,
      // need to add book name
      newBook: {
        isbn: null,
        name: "",
        category: "",
        author: ""
      },
      bookFillInfo: {
        dat: {
          isbn: "",
          name: "",
          category: "",
          author: ""
        }
      },
      deletedID: null,
      deletedIDOption: [],
      showDeleteModal: false,
      showAddModal: false,
      // filterFeature
      currentPage: 1,
      perPage: 5,
      pageOptions: [1, 5, 10, 15],
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      filter: null,
      filterOn: []
    };
  },
  mounted() {
    this.fetchBooks();
  },
  computed: {
    ...mapState({
      isLoading: state => state.book.isLoading,
      isSuccess: state => state.book.isSuccess,
      isError: state => state.book.isError,
      books: state => state.book.books,
      totalRows: state => state.book.books.length,
      bookdict: state => state.book.bookdict,
      isbns: state => state.book.isbns
    }),
    isbnISMatch: function() {
      if (typeof this.bookFillInfo == "undefined") {
        return false;
      }
      return this.isbns.includes(this.bookFillInfo.dat.isbn);
    },
    isBookInfoRestrict: function() {
      if (this.isbnISMatch) {
        return true;
      } else {
        return false;
      }
    }
  },
  watch: {
    isbnISMatch: function() {
      if (this.isbnISMatch) {
        this.restrictBookInfo();
      }
    }
  },

  methods: {
    onFiltered(filteredItems) {
      this.$store.dispatch('book/setTotalRow',)
      totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    showDeleteConfirm(id) {
      this.$bvModal
        .msgBoxConfirm("Please confirm that you want to delete.", {
          title: "Please Confirm",
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
            // alert(item.GadgetID)
            this.deleteBook(id);
            this.showDeleteModal = false;
          } else {
            // asdasda
            this.showDeleteModal = true;
          }
        });
    },
    fillData(item = null, option = null) {
      if (option != "ADD MORE") {
        this.bookFillInfo.dat.isbn = "";
        this.bookFillInfo.dat.name = "";
        this.bookFillInfo.dat.category = "";
        this.bookFillInfo.dat.author = "";
        this.showAddModal = true;
      } else {
        // OPTION IS ADD
        this.bookFillInfo.dat.isbn = item.isbn;
        this.bookFillInfo.dat.name = item.name;
        this.bookFillInfo.dat.category = item.category;
        this.bookFillInfo.dat.author = item.author;
      }
    },
    loadRowData(item, option) {
      if (option == "ADD MORE") {
        this.fillData(item, option);
        this.showAddModal = true;
      } else {
        this.deletedIDOption = item.number;
        this.showDeleteModal = true;
      }
    },
    restrictBookInfo() {
      this.bookFillInfo.dat.name = this.bookdict[this.bookFillInfo.dat.isbn][
        "name"
      ];
      this.bookFillInfo.dat.category = this.bookdict[
        this.bookFillInfo.dat.isbn
      ]["category"];
      this.bookFillInfo.dat.author = this.bookdict[this.bookFillInfo.dat.isbn][
        "author"
      ];
    },
    fetchBooks: function() {
      // alert("start fetch");
      this.$store.dispatch("book/fetchBooks");
    },
    addBook: function(restrict) {
      // console.log(this.bookFillInfo.dat);
      let res;
      if (restrict) {
        res = {
          isbn: this.bookFillInfo.dat.isbn,
          name: "",
          category: "",
          author: ""
        };
      } else {
        res = {
          isbn: this.bookFillInfo.dat.isbn,
          name: this.bookFillInfo.dat.name,
          category: this.bookFillInfo.dat.category,
          author: this.bookFillInfo.dat.author
        };
      }
      this.$store.dispatch("book/postBooks", res);
      this.showAddModal = false;
    },
    deleteBook: function(id) {
      this.$store.dispatch("book/deleteBooks", id);
    }
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
