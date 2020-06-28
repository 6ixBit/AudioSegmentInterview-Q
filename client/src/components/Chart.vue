<template>
  <div>
    <apexchart
      width="400"
      type="bar"
      :options="options"
      :series="series"
    ></apexchart>
  </div>
</template>

<script>
export default {
  props: ["option1", "series1", "result"],
  data: function() {
    return {
      options: {},
      series: []
    };
  },
  methods: {
    formatData(data) {
      let parsedobj     = JSON.parse(JSON.stringify(data)); //Decode response
      let seriesData    = []
      let xAxisColumns  = []

      Object.keys(parsedobj).forEach(key => {
        xAxisColumns.push(key)
        seriesData.push(data[key]['timesTalked'])
      });

      // Set state for charts.
      this.options = {
        chart: {
          id: "audio-segments"
        },
        xaxis: {
          categories: xAxisColumns
        }
      }

      this.series = [
        {
          data: seriesData
        }
      ]
    }
  },
  watch: {
    result: function(newVal) {
      this.formatData(newVal)
    }
  }
};
</script>
