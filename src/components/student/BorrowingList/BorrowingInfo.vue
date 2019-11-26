<template>
  <b-container>
    <b-table :items="borrows" :fields="fields" striped responsive="sm">
      <template v-slot:cell(Renew)="row">
          <b-button v-if="diffDate(row.item.ReturnDate)<=3 && diffDate(row.item.ReturnDate)>=0" @click="setModal(row.item)" size="sm" variant="primary" class="m-2">renew</b-button>
          <b-button v-else @click="setModal(row.item)" disabled size="sm" class="m-2">renew</b-button>
      </template>
    </b-table>

    <!-- Update Modal -->
    <b-modal
      id="modal-renew-update"
      ref="modal"
      title="Renew Time"
      @ok="handleOk()"
    >
    <p>Confirm renew time</p>
    </b-modal>
    <!--End of Update Modal -->
  </b-container>
</template>

<script>
import { mapState } from "vuex";
import moment from "moment";
export default {
  name: "BorrowingInfo",
  props: {},
  components: {},
  data() {
    return {
      fields: [
        "ID",
        "BookName",
        "BorrowDate",
        "ReturnDate",
        "RenewTime",
        "Renew"
      ],
      renew: {
        'EndDate': '',
        'RenewTimes': '',
        'id': '',
      }
    };
  },
  methods: {
    setModal(item) {
      let date = new Date(item.ReturnDate);
      date.setDate(date.getDate()+7);
      let month = date.getUTCMonth()+1;
      this.renew.EndDate = date.getFullYear()+'-'+month+'-'+date.getDate();
      this.renew.RenewTimes = item.RenewTime-1;
      this.renew.id = item.ID;
      this.$refs.modal.show();
    },
    handleOk() {
      if (this.renew.RenewTimes < 0) {
        alert("Can not renew time");
        return;
      }
      this.$store.dispatch("borrowing/updateRenewTime", this.renew);
      this.$nextTick(() => this.$refs.modal.hide());
    },
    diffDate(date){
      return moment.duration((moment(date)).diff(moment())).asDays()
    }
    //end of update modal
  },
  computed: {
    ...mapState({
      borrows: state => state.borrowing.borrows
    })
  },
  mounted() {
    this.$store.dispatch("borrowing/getBorrow", "student1");
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
