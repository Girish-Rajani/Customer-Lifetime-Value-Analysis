# Customer Lifetime Value Analysis

## Overview

The Customer Lifetime Value (CLTV) Analysis project aims to evaluate the effectiveness and efficiency of various customer acquisition channels by analyzing cost per conversion, revenue per conversion, and overall return on investment (ROI). The analysis is conducted using Python and various data visualization libraries to gain insights into how different marketing channels contribute to customer acquisition.

## Exploratory Data Analysis (EDA) Performed:

### Customer Acquisition Cost (CAC) by Channel

![customer_acquistion_cost_by_channel](https://github.com/user-attachments/assets/ec383ee7-9a7f-40bb-923d-f59e29e2bec7)

As shown above, email marketing has the lowest CAC which proves to be the most cost-effective for acquiring new customers while Paid Advertising has the opposite effect. This is an expected outcome, however, to further understand the value that each of these channel bring, we need to further explore other metrics to understand if the extra CAC for paid advertising is worth the cost.

### Conversion Rate and Cost per Conversion by Channel

![conversion_rate_by_channel](https://github.com/user-attachments/assets/eb642558-e8bc-40bc-909f-333c352ba25b)

![cost_per_conversion_by_channel](https://github.com/user-attachments/assets/bc1b836b-85c5-49c8-8932-f8700bba4aa2)

As shown above, social media and referrals had the highest conversion rate as well as lowest cost per conversion. This means that these two channels are great for getting users to take action. Perhaps email marketing and paid advertising shine bright for other sections in the customer journey funnel as will be explored further below.

### Revenue and Revenue per Conversion by Channel

![total_revenue_by_channel](https://github.com/user-attachments/assets/51c66b69-75d3-445d-bf0e-f11ff64e57f2)

![revenue_per_conversion_by_channel](https://github.com/user-attachments/assets/490266d4-504b-443a-85d2-be4275451577)

As shown above, all channels have similar total revenue, with email marketing being slightly higher than all. However, we can explore revenue per conversion to see the average amount earned from each conversion and email marketing and paid advertising are the top. This means that as shown before, even though these two channels may have the highest cost per conversion, they also have the highest revenue per conversion. This should balance out as we look into ROI next.

### Return on Investment (ROI) by Channel

![roi_by_channel](https://github.com/user-attachments/assets/d022844d-3ed7-43b5-be75-684f09439b8e)

As shown above, all three channels except for paid advertising have a relatively large ROI. Although paid advertising yields high revenue per conversion, it also has a very high cost per conversion and customer acquisition cost which shows that this channel should be optimized.
Email marketing is highly cost-effective returns a large amount of revenue for every dollar spent. This patter was observed with a high revenue per conversion and low customer acquisition cost.

### CLTV by Channel

![cltv_by_channel](https://github.com/user-attachments/assets/8537fe2d-7b48-419b-bfd1-28f3acc2c9a6)

![cltv_distribution_by_channel](https://github.com/user-attachments/assets/707d7fec-147c-4392-8c5e-c793b22136f3)

When looking at the bigger picture, Customer LIfetime Value (CLTV), we see that social media and referrals have the highest CLTV while paid advertising has the least. This paints a picture that social media and referrals are able to hold customers for a long time, perhaps they are able to resonate with the brand values better. 

## Conclusion

In conclusion, different channels work better at different stages of the marketing funnel. However, in this case, it was consistently seen that at each stage of the marketing funnel, paid advertising had a high cost (whether in acquisition or conversion) while also having relatively low revenue and conversion rates. Additionally, long term, the Customer Lifetime Value (CLTV) was also lowest for paid advertising. Referrals and Social Media channels had the largest CLTV indicating long term retention efforts should be focused on these channels while also optimizing other channels.
This project builds on the foundational work provided in The Clever Programmer's Customer Lifetime Value Analysis using Python by expanding the analysis to provide deeper insights into various other aspects of the CLTV analysis. 

## References

 1. [Customer Success Metrics](https://blog.hubspot.com/service/customer-success-metrics)
 2. [Project Reference](https://thecleverprogrammer.com/2023/01/16/ads-click-through-rate-prediction-using-python/)
 3. [Dataset](https://statso.io/customer-lifetime-value-analytics-case-study/)
 
