<template>
  <div class="jumbotron bg-overlay">
    <h2>
      Book
      <b-button v-b-modal.modal-add-book>ADD BOOK</b-button>
    </h2>
    <!-- Add Book Modal -->
    <b-modal id="modal-add-book" title="ADD BOOK">
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
    <b-modal id="modal-delete-book" title="DELETE BOOK" v-model="show" hide-footer>
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
        <button type="button" class="btn btn-danger" @click="showDeleteConfirm(deletedID)" data-dismiss="modal">OK</button>
      </div>
    </b-modal>

    <b-table :items="books" :fields="fields" striped responsive="sm">
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
          <b-button size="lg" variant="danger" class="m-2" v-b-modal.modal-delete-book @click="loadRowData(row.item.number)">Delete</b-button>
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
        { key: "isbn", label: "ISBN" },
        { key: "name", label: "BookName" },
        { key: "category", label: "Category" },
        { key: "author", label: "Author" },
        { key: "num", label: "Count" },
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
      show :false,
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
            this.show = false
          } else {
            // asdasda
            this.show = true
          }
        });
    },
    loadRowData(options) {
      this.deletedIDOption = options
      this.show =true
    },
    restrictBookInfo() {
      this.bookFillInfo.dat.name = this.bookdict[this.bookFillInfo.dat.isbn][
        "name"
      ]
      this.bookFillInfo.dat.category = this.bookdict[
        this.bookFillInfo.dat.isbn
      ]["category"]
      this.bookFillInfo.dat.author = this.bookdict[this.bookFillInfo.dat.isbn][
        "author"
      ]
    },
    fetchBooks: function() {
      // alert("start fetch");
      this.$store.dispatch("book/fetchBooks");
    },
    addBook: function(restrict) {
      // console.log(this.bookFillInfo.dat);
      let res
      if(restrict) {
         res = {
          "isbn": this.bookFillInfo.dat.isbn,
          "name": "",
          "category": "",
          "author": ""
        }
      } else {
        res = {
          "isbn": this.bookFillInfo.dat.isbn,
          "name": this.bookFillInfo.dat.name,
          "category": this.bookFillInfo.dat.category,
          "author": this.bookFillInfo.dat.author
        }
      }
      this.$store.dispatch("book/postBooks", res);
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
