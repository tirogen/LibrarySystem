<template>
  <div class="jumbotron bg-overlay">
    <h2>Book
    <b-button v-b-modal.modal-1>ADD BOOK</b-button>
    </h2>
    <!-- Add Book Modal -->
    <b-modal id="modal-2" title="BootstrapVue">
        <div class="modal-content">
            <div class="modal-body">
                  <label for="newBook">Book THING</label>
                  <input
                    type="text"
                    class="form-control"
                    id="BookName"
                    placeholder="Enter Book Name"
                    v-model="newBook.id"
                    required="required">
            </div>
        </div>
      <template v-slot:modal-footer="{ ok, cancel }">
        <b>Custom Footer</b>
        <!-- Emulate built in modal footer ok and cancel button actions -->
        <b-button size="sm" variant="success" v-on:click="addBook()">
          OK
        </b-button>
        <b-button size="sm" variant="danger" @click="cancel()">
          Cancel
        </b-button>
      </template>
    </b-modal>
    <!-- End of add Book modal -->
    <b-table :items="books" :fields="fields" striped responsive="sm">
      <template v-slot:cell(Manage)="row">
        <b-button size="sm" @click="row.toggleDetails" class="mr-2">
          {{ row.detailsShowing ? 'Hide' : 'Show'}} Manage
        </b-button>
      </template>
      <template v-slot:row-details="row">
        <b-card>
          <b-button size="sm" variant="primary" class="m-2">Check in</b-button>
          <b-button size="sm" variant="danger" class="m-2">Delete</b-button>
        </b-card>
      </template>
    </b-table>
    <b-button block variant="primary">See all</b-button>
  </div>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name: 'Book',
  props: {

  },
  data() {
    return {
      fields: ['id', 'ISBN', 'Status', 'Manage'],
      // need to add book name
      newBook: { 'id': null, 'ISBN': null, 'status': null}
    }
  },
  mounted() {
   this.fetchBooks();
  },
  computed: mapState({
    isLoading: state => state.book.isLoading,
    isSuccess: state => state.book.isSuccess,
    isError: state => state.book.isError,
    books: state => {
      return state.book.books
    }
  }),

  methods: {
    fetchBooks: function(){
        this.$store.dispatch('book/getBooks')
    },
    addBook: function(){
      this.$store.dispatch('book/add', this.newBook)
    }
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
