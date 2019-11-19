import StudentLayout from './index.vue'
import Student from './Student.vue'
import ReserveRoom from './ReserveRoom/index.vue'

export const studentRoutes = {
  path: '/student',
  component: StudentLayout,
  children: [
    {
      path: '',
      name: 'student',
      component: Student
    },
    {
      path: 'reserve-room',
      component: ReserveRoom
    }
  ]
}

export default studentRoutes