<script>
    //Step 1 : import dependecies
    import FroalaCharts from "froalacharts";
    import FroalaTheme from "froalacharts/themes/froalacharts.theme.froala";
    import SvelteFC, { fcRoot } from "svelte-froalacharts";
    import Test from "./data-classes/test-data.js"
    // Always set FroalaCharts as the first parameter
    fcRoot(FroalaCharts, FroalaTheme);
    export let yaxis;
    var t = new Test();
    //Step 2: preparing the chart Data
    const chartData = [
    {
      data: t.data1
    }];
    
    //Step 3 : Create your configuration object
    export let chartConfig = {
      type: "line",
      renderAt: "ft",
      width: "1850",
      height: "502",
      dataSource:
      {
        chart:
        {
          theme: "froala",
          caption: "Comparison of Quarterly Revenue",
          xAxisname: "Quarter",
          yAxisName: yaxis,
          numberPrefix: "$",
        },
        categories: [
        {
          category: [
          {
            label: "Q1",
          },
          {
            label: "Q2",
          },
          {
            label: "Q3",
          },
          {
            label: "Q4",
          }
          ,
          {
            label: "Q5",
          }
          ,
          {
            label: "Q6",
          },
          {
            label: "Q7",
          }]
        }],
        dataset: chartData
      }
    }; 
    </script>
    
<main>
    <div class="chart">
        <SvelteFC {...chartConfig}/>
    </div>
</main>

<style>
    .chart{
        border:4px solid;
    }
</style>