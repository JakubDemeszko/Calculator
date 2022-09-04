{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b419d4ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The highest value is in index: 31673\n",
      "Year                             2012\n",
      "Make                       Mitsubishi\n",
      "Model                          i-MiEV\n",
      "Class                 Subcompact Cars\n",
      "Fuel Type                 Electricity\n",
      "Combined MPG (FT1)              112.0\n",
      "Name: 31673, dtype: object\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Combined MPG (FT1)</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Vehicle ID</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>26587</th>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27705</th>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26561</th>\n",
       "      <td>10.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27681</th>\n",
       "      <td>10.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27550</th>\n",
       "      <td>8.5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Combined MPG (FT1)\n",
       "Vehicle ID                    \n",
       "26587                     10.0\n",
       "27705                     10.0\n",
       "26561                     10.5\n",
       "27681                     10.5\n",
       "27550                      8.5"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# The goal in this simple task is to find some maximum values from Data Frame and then get full information.\n",
    "\n",
    "cars = fuel = pd.read_csv(\"C:/Users/demes/Downloads/data/course-files/fuel.csv\",\n",
    "low_memory = False, usecols = ['Vehicle ID','Year','Make','Model','Class','Fuel Type','Combined MPG (FT1)'], \n",
    "index_col = [\"Vehicle ID\"])\n",
    "# Finding the value highest value in column to 'Combined MPG (FT1)'\n",
    "\n",
    "print(\"The highest value is in index:\", cars['Combined MPG (FT1)'].idxmax())\n",
    "\n",
    "print(cars.loc[31673])\n",
    "\n",
    "# Creating some other Data Frame from existing one and then counting it as a KPI value.\n",
    "\n",
    "carsSeries = cars[['Combined MPG (FT1)']]\n",
    "\n",
    "target_values = carsSeries * 0.5\n",
    "target_values.head()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
