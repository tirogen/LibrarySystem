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
    // alert(JSON.stringify(newGadget))
      return api.post('Gadget/manageGadget/',JSON.stringify(newGadget)).then(response => {
        // alert(JSON.stringify(response.data))
        alert("new gadgets coming")
        return response.data
      })
    .catch((e) => {
      console.log("error new state : ", e)
    })

  },
  deleteGadget(index) {
      return api.delete('Gad/get/manageGadget/', index).then(response => {

        return response
      })
  },
  updateGadget(newUpdatedGadget) {
    return api.update('Gadget/manageGadget/',JSON.stringify(newUpdatedGadget)).then(response => {
      // alert(JSON.stringify(response.data))
      alert("new update coming")
      return response
    })
  }
  
}