<template>
  <div class="container">
    <br>
    <Borrow />
    <Book />
    <Gadget />
    <LibrarianRoomType />
    <LibrarianRoom />
    <LibrarianReserved />
    <LibrarianPunish />
  </div>
</template>

<script>
import LibrarianReserved from "./LibrarianReserved";
import LibrarianPunish from "./LibrarianPunish/LibrarianPunish";
import Gadget from "./LibrarianGadget";
import Book from "./LibrarianBook";
import Borrow from "./LibrarianManageBorrow";
import LibrarianRoomType from "./LibrarianRoomType";
import LibrarianRoom from "./LibrarianRoom";

export default {
  name: "Librarian",
  props: {},
  components: {
    Borrow,
    LibrarianReserved,
    Gadget,
    LibrarianPunish,
    Book,
    LibrarianRoomType,
    LibrarianRoom
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
