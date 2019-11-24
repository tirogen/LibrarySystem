<template>
  <div class="container">
    <b-nav-item href="#borrow">Book Borrow</b-nav-item>|
    <b-nav-item href="#book">Book Manage</b-nav-item>|
    <b-nav-item href="#gadget">Gadget Manage</b-nav-item>|
    <b-nav-item href="#roomType">Room Type</b-nav-item>|
    <b-nav-item href="#room">Room Manage</b-nav-item>|
    <b-nav-item href="#reserve">Reserve Room</b-nav-item>|
    <b-nav-item href="#punish">Punish Manage</b-nav-item>
    <section
      id="borrow"
      data-aos="fade-up"
      data-aos-offset="200"
      data-aos-delay="50"
      data-aos-duration="600"
      data-aos-easing="ease-in-out"
      data-aos-mirror="true"
      data-aos-once="false"
      data-aos-anchor-placement="top-center"
    >
      <Borrow />
    </section>
    <section
      id="book"
      data-aos="fade-up"
      data-aos-offset="200"
      data-aos-delay="50"
      data-aos-duration="600"
      data-aos-easing="ease-in-out"
      data-aos-mirror="true"
      data-aos-once="false"
      data-aos-anchor-placement="top-center"
    >
      <Book />
    </section>
    <section
      id="gadget"
      data-aos="fade-up"
      data-aos-offset="200"
      data-aos-delay="50"
      data-aos-duration="600"
      data-aos-easing="ease-in-out"
      data-aos-mirror="true"
      data-aos-once="false"
      data-aos-anchor-placement="top-center"
    >
      <Gadget />
    </section>
    <section
      id="roomType"
      data-aos="fade-up"
      data-aos-offset="200"
      data-aos-delay="50"
      data-aos-duration="600"
      data-aos-easing="ease-in-out"
      data-aos-once="false"
      data-aos-anchor-placement="top-center"
    >
      <LibrarianRoomType />
    </section>
    <section
      id="room"
      data-aos="fade-up"
      data-aos-offset="200"
      data-aos-delay="50"
      data-aos-duration="600"
      data-aos-easing="ease-in-out"
      data-aos-once="false"
      data-aos-anchor-placement="top-center"
    >
      <LibrarianRoom />
    </section>
    <section
      id="reserve"
      data-aos="fade-up"
      data-aos-offset="200"
      data-aos-delay="50"
      data-aos-duration="600"
      data-aos-easing="ease-in-out"
      data-aos-once="false"
      data-aos-anchor-placement="top-center"
    >
      <LibrarianReserved />
    </section>
    <section
      id="punish"
      data-aos="fade-up"
      data-aos-offset="200"
      data-aos-delay="50"
      data-aos-duration="600"
      data-aos-easing="ease-in-out"
      data-aos-once="false"
      data-aos-anchor-placement="top-center"
    >
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
