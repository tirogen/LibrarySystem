export const baseState = {
    isLoading: false,
    isSuccess: false,
    isError: false,
    errorData: null,
}

export const baseMutation = {
    loading: (state) => {
        state.isLoading = true
        state.isSuccess = false
        state.isError = false
    },
    success: (state) => {
        state.isSuccess = true
        state.isError = false
        state.isLoading = false
    },
    error: (state) => {
        state.isError = true
        state.isSuccess = false
        state.isLoading = false
    }
}