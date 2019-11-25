<template>
  <div class="jumbotron bg-overlay">
    <h2>
      Borrowing Book
    </h2>
    <b-tabs>
      <b-tab title="Borrowing">
        <BorrowingInfo></BorrowingInfo>
      </b-tab>
    </b-tabs>
  </div>
</template>
<script>
import {mapState} from 'vuex'
import BorrowingInfo from './BorrowingInfo.vue'
export default {
  name: 'BorrowingList',
  props: {

  },
  components: {
    BorrowingInfo,
  },
  data() {
    return {
      fields: ['ID', 'BookName', 'BorrowDate', 'ReturnDate', 'RenewTime'],

    }
  },
  methods: {
    
    //end of add modal
  },
  computed: mapState({
    borrows: state => state.borrowing.borrows
  }),
  mounted(){
    this.$store.dispatch('borrowing/getBorrow','student1')
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
