import json

sample_tweets = {}

sample_tweets['mumbai'] = list(['At all PDS centers wheat and rice available fr jst re 3 and 4 per kg bt congress govt in maharashtra is lazy and v nikammi',
                                '@thekiranbedi @sardesairajdeep  PDS-Rs 15 per kg Rice  amp  20per kg Wheat goes to hotels imagine wht will happen to Rs 2Kg rice  amp  Rs 3 kg wheat',
                                '1 rice bowl Rs 500  Uttarakhand  shame',
                                '@suhelseth Onion has got a companion in the form of Tomato   Do you believe Rs  60 for a Kg      Somebody should wake up our PM',
                                'Anyone offering  Gold  Loan         Want to buy  1kg  Onion please',
                                'congress economic policy-onion 70/kg potato 32/kg tomato 75/kg price doubled in few weeks',
                                'rs 10 - per kg onion  rs 10 - per kg potato  at big bazaar RCiti mall ghatkopar'
                                ])

sample_tweets['bangalore'] = list(['@DrShobha One cup of rice 500 Rs  One Paratha or Roti 250 Rs  One chips Packet 100 Rs  Water bottle 100 Rs  Have some Mercy',
                                   '@divyaspandana in banglore the tomato prices are 50rs and onion 50rs  plz worry abt these issue which affect common man y r u wasting time',
                                   'What is happening with Indian Economy everything goes up Rupees value 65 as compared to     now onion price also:-  touched 80  unbearable',
                                   'Soon Rupee wil touch Rs 100   1  Petrol will be Rs 100 Ltr  Onion Rs 100 kg    Still so much of drama amp politics in Parliament amp  war mongering',
                                   'Inflation of food items shot up by 13 39 per cent during the week ended October 24 driven mainly by soaring prices of potato and onion'
                                   ])

sample_tweets['chennai'] = list(['Onion is costly  but penion is not even sold  Male chauvinistic India   onioncrisis',
                                   'a friend was telling me other day that vegetable price rise may bring down the govt Oil price rise did not what will onion tomato  eggs do',
                                   'Is it true dat sans taxes oil wl be 20 Rs ltr   read it sumwhr   bt nt sure',
                                   'Oil Rises Above  74 on Bets Demand Will Gain on U S  Economy'
                                   ])

sample_tweets['kolkata'] = list(['Now potato prices going bonkers in WB   50 this afternoon',
                                 'What a country  Were 1 Kg potato costs Rs 25 as 6 months earlier it costed Rs 8  In Asansol policemen are selling potatoes as the C M  :',
                                 'potato prices are up by 25  in Bengal in a week as sowing season delayed by a fortnight due to rains',
                                 'timesnow So is Potato prices jumped 40  in a week  cong busy in making Bills'
                                 ])

sample_tweets['hyderabad'] = list(['Tasty chicken momo for just Rs 50 a plate :D    Himalaya Momo  http:  t co 4kHxGOmH',
                                   'First tym in india need  comfort and luxury r available at same price   Onion 75 rs   Petrol 75 rs   Beer   75 rs',
                                   'Onion prices will stabilise after 3 weeks: Sharad Pawar'
                                   ])

with open("tweet_samples_by_city.json", "w") as outfile:
    json.dump(sample_tweets, outfile)
