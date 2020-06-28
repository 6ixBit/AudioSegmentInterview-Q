<template>
    <div class="table">
        <b-table :items="res" :fields="fields">
            <template v-slot:table-caption>Amount of times an individual talked</template>
        </b-table>
    </div>
</template>

<script>
export default {
    props: ['data'],
    data() {
        return {
            fields: ['Name', 'Total_Contributions', 'Average_Contributions'],
            res: []
        }
    },
    methods: {
        formatData(data) {
            let parsedobj = JSON.parse(JSON.stringify(data))
    
            Object.keys(parsedobj).forEach(key => {
                let row = {
                    Name:               key,
                    Total_Contributions:     data[key]['callContributions'],
                    Average_Contributions:   data[key]['avgCallContributions']
                }
                this.res.push(row)
            });
        }
    },
    watch: {
        data: function (newVal) {
            this.formatData(newVal)
        }
    }
}
</script>

<style scoped>
    .table {
        margin: 50px 5px
    }
</style>