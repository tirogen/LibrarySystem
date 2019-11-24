<template>
  <div class="container">
    <b-nav-item href="#borrow">Book Borrow</b-nav-item>|
    <b-nav-item href="#book">Book Manage</b-nav-item>|
    <b-nav-item href="#gadget">Gadget Manage</b-nav-item>|
    <b-nav-item href="#room">Room Manage</b-nav-item>|
    <b-nav-item href="#reserve">Reserve room</b-nav-item>|
    <b-nav-item href="#punish">Punish Manage</b-nav-item>
    <section id="borrow">
      <Borrow />
    </section>
    <section id="book">
      <Book />
    </section>
    <section id="gadget">
      <Gadget />
    </section>
    <section id="room">
      <LibrarianRoomType />
    </section>
    <section id="reserve">
      <LibrarianReserved />
    </section>
    <section id="punish">
      <LibrarianPunish />
    </section>
  </div>
</template>

<script>
import LibrarianReserved from "./LibrarianReserved";
import LibrarianPunish from "./LibrarianPunish/LibrarianPunish";
import Gadget from "./LibrarianGadget";
import Book from "./LibrarianBook";
import Borrow from "./LibrarianManageBorrow";
import LibrarianRoomType from "./LibrarianRoomType";

export default {
  name: "Librarian",
  props: {},
  components: {
    Borrow,
    LibrarianReserved,
    Gadget,
    LibrarianPunish,
    Book,
    LibrarianRoomType
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
