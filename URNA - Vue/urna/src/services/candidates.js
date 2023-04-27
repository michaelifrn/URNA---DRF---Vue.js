import { http } from './api'

export default {

    list:() => {
        return http.get('candidate/')
    },

    vote:(vote) =>{
        return http.post('vote/', vote)
    },

    voteList:() => {
        return http.get('vote/')
    },

    report:() => {
        return http.get('report/')
    }
}