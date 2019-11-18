import api from '@/services/api'

export default {
  fetchGadgets() {
    return api.get(`Gadget/getGadget/`)
              .then(response => response.data)
  },
  fectchRooms() {
    return api.get('Room/getRoom/')
              .then(response => response.data)
  },
  postGadget(newGadget) {

    return api.post('Gadget/getGadget/', {
    firstName: 'Fred',
    lastName: 'Flintstone'
  }) 
              .then(response => response)
  } 
  
}