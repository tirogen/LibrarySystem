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
        // alert("new gadgets coming")
        return response.data
      })
    .catch((e) => {
      console.log("error new state : ", e)
    })

  },
  deleteGadget(id) {
      return api.delete(`Gadget/manageGadget/${id}`).then(response => {
        return response.data
      })
  },
  updateGadget(newUpdatedGadget) {
    return api.put('Gadget/manageGadget/',JSON.stringify(newUpdatedGadget)).then(response => {
      // alert(JSON.stringify(response.data))
      // console(response.status)
      // alert("new update coming")
      return response.data
    })
  }
  
}