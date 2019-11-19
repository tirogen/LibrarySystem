import api from '@/services/api'
const qs = require('qs');

export default {
  fetchGadgets() {
    return api.get(`Gadget/getGadget/`)
              .then(response => response.data)
  },
  fetchRooms() {
    return api.get('reservedRoom/getRoom')
              .then(response => response.data)
  },
  postGadget(newGadget) {
    return api.post('Gadget/getGadget/',qs.stringify(newGadget)).then(response => response.data
    )
    .catch((e) => {
      console.error(e)
    })

  } 
  
}