import api from '@/services/api'
export default {
  fetchGadgets() {
    return api.get(`Gadget/manageGadget/`)
              .then(response => response.data)
  },
  fetchRooms() {
    return api.get('reservedRoom/manageRoom')
              .then(response => response.data)
  },
  postGadget(newGadget) {
    alert(JSON.stringify(newGadget))
    return api.post('Gadget/manageGadget/',JSON.stringify(newGadget)).then(response => response.data
    )
    .catch((e) => {
      console.error(e)
    })

  } 
  
}