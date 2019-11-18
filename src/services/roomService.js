import api from '@/services/api'

export default {
  fetchGadgets() {
    return api.get(`Gadget/getGadget/`)
              .then(response => response.data)
  },
  fectchRooms() {
    return api.get('reservedRoom/getRoom')
              .then(response => response.data)
  },
  postGadget(newGadget) {
    return api.post('Gadget/getGadget/', {
      title: "asdasd",
      body: "asd"
    }).then((response) => {
      response => response.data
    })
    .catch((e) => {
      console.error(e)
    })

  } 
  
}