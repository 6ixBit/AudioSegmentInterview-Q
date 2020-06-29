<template>
    <div>
        <b-container class="bv-example-row">

            <b-row class="justify-content-md-center"> <!-- TITLE -->
                <b-col cols="12" md="auto">
                    <h1 class="title">Combine AI Audio Segments</h1>
                </b-col>
            </b-row>
       
            <b-row class="justify-content-md-center">
                <b-col cols="12" md="auto"> <!-- GRAPH -->

                    <Chart :result="this.result"></Chart>
                </b-col>
            </b-row>

            <b-row class="justify-content-md-center"> <!-- TABLE -->
                <b-col cols="12" md="auto">
                    <Table :data="result"> </Table>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import axios from 'axios'
import Table from './Table'
import Chart from './Chart'

export default {
    components : {
        "Table" : Table,
        "Chart" : Chart
    },
    data() {
        return {
            result: [],
            serverURL: "http://localhost:5000/stat", // For deployment
            plyr: "Neo"
        }
    },
    methods: {
        async fetchAllStats() {
            try {
                let res = await axios.get(this.serverURL+"/all")
                this.result = res.data

            } catch (e) {
                console.log(e)
            }
        }, 
        async removeParticipant(name) {
            try {
                // Logic to remove
                for (let el in this.result) {
                    if (name === el) {
                        delete this.result[name]
                        console.log(this.result)
                    }
                }
            } catch(e) {
                console.log(e)
            }
        }
    }, 
    async mounted () {
        try {
            await this.fetchAllStats()
        } catch (e) {
            console.log(e)
        }
    }
}
</script>

<style scoped>
    .title {
        margin: 3px 5px
    }
</style>