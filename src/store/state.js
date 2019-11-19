export const baseState = {
  isLoading: false,
  isSuccess: false,
  isError: false,
  errorData: null,
}

export const baseMutations = {
  loading(state) {
    state.isLoading = true
    state.isSuccess = false
    state.isError = false
  },
  success(state) {
    state.isSuccess = true
    state.isError = false
    state.isLoading = false
  },
  error(state, errorData) {
    state.errorData = errorData
    state.isError = true
    state.isSuccess = false
    state.isLoading = false
  }
}