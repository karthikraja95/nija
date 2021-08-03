import numpy as np
import pandas as pd
import sklearn
import warnings
import math

from nyx.config.config import _global_config
from .model_analysis import SupervisedModelAnalysis

class RegressionModelAnalysis(SupervisedModelAnalysis):
    def __init__(
        self, model, x_train, x_test, target, model_name,
    ):
        """
        Class to analyze Regression models through metrics, global/local interpretation and visualizations.
        Parameters
        ----------
        model : str or Model Object
            Sklearn, XGBoost, LightGBM Model object or .pkl file of the objects.
        x_train : pd.DataFrame
            Training Data used for the model.
        x_test : pd.DataFrame
            Test data used for the model.
        target : str
            Target column in the DataFrame
        model_name : str
            Name of the model for saving images and model tracking purposes
        """

        # TODO: Add check for pickle file

        super().__init__(
            model,
            x_train.drop([target], axis=1),
            x_test.drop([target], axis=1),
            x_train[target],
            x_test[target],
            model_name,
        )

    def plot_predicted_actual(self, output_file="", **scatterplot_kwargs):
        """
        Plots the actual data vs. predictions
        Parameters
        ----------
        output_file : str, optional
            Output file name, by default ""
        """

        self._viz.scatterplot(
            x="actual",
            y="predicted",
            data=self.test_results,
            title="Actual vs. Predicted",
            output_file=output_file,
            **scatterplot_kwargs
        )

    def explained_variance(self, multioutput="uniform_average", **kwargs):
        """
        Explained variance regression score function
        Best possible score is 1.0, lower values are worse.
        
        Parameters
        ----------
        multioutput : string in [‘raw_values’, ‘uniform_average’, ‘variance_weighted’] or array-like of shape (n_outputs)
            Defines aggregating of multiple output scores. Array-like value defines weights used to average scores.
            ‘raw_values’ :
                Returns a full set of scores in case of multioutput input.
            ‘uniform_average’ :
                Scores of all outputs are averaged with uniform weight.
            ‘variance_weighted’ :
                Scores of all outputs are averaged, weighted by the variances of each individual output.
            By default 'uniform_average'
        
        Returns
        -------
        float
            Explained Variance
        Examples
        --------
        >>> m = model.LinearRegression()
        >>> m.explained_variance()
        """

        return sklearn.metrics.explained_variance_score(
            self.y_test, self.y_pred, multioutput="uniform_average", **kwargs
        )

    def max_error(self):
        """
        Returns the single most maximum residual error.
        
        Returns
        -------
        float
            Max error
        Examples
        --------
        >>> m = model.LinearRegression()
        >>> m.max_error()
        """

        return sklearn.metrics.max_error(self.y_test, self.y_pred)

    def mean_abs_error(self, **kwargs):
        """
        Mean absolute error.
        
        Returns
        -------
        float
            Mean absolute error.
        Examples
        --------
        >>> m = model.LinearRegression()
        >>> m.mean_abs_error()
        """

        return sklearn.metrics.mean_absolute_error(self.y_test, self.y_pred)

    def mean_sq_error(self, **kwargs):
        """
        Mean squared error.
        
        Returns
        -------
        float
            Mean squared error.
        Examples
        --------
        >>> m = model.LinearRegression()
        >>> m.mean_sq_error()
        """

        return sklearn.metrics.mean_squared_error(self.y_test, self.y_pred)

    def mean_sq_log_error(self, **kwargs):
        """
        Mean squared log error.
        
        Returns
        -------
        float
            Mean squared log error.
        Examples
        --------
        >>> m = model.LinearRegression()
        >>> m.mean_sq_log_error()
        """

        try:
            return sklearn.metrics.mean_squared_log_error(self.y_test, self.y_pred)
        except ValueError as e:
            warnings.warn(
                "Mean Squared Logarithmic Error cannot be used when targets contain negative values."
            )
            return -999

    def median_abs_error(self, **kwargs):
        """
        Median absolute error.
        
        Returns
        -------
        float
            Median absolute error.
        Examples
        --------
        >>> m = model.LinearRegression()
        >>> m.median_abs_error()
        """

        return sklearn.metrics.median_absolute_error(self.y_test, self.y_pred)

    def r2(self, **kwargs):
        """
        R^2 (coefficient of determination) regression score function.
        R-squared (R2) is a statistical measure that represents the proportion of the variance for a dependent variable
        that is explained by an independent variable or variables in a regression model.
        Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse).
        A constant model that always predicts the expected value of y, disregarding the input features, would get a R^2 score of 0.0.
        
        Returns
        -------
        float
            R2 coefficient.
        Examples
        --------
        >>> m = model.LinearRegression()
        >>> m.r2()
        """

        return sklearn.metrics.r2_score(self.y_test, self.y_pred)

    def smape(self, **kwargs):
        """
        Symmetric mean absolute percentage error.
        It is an accuracy measure based on percentage (or relative) errors.
        
        Returns
        -------
        float
            SMAPE
        Examples
        --------
        >>> m = model.LinearRegression()
        >>> m.smape()
        """

        return (
            1
            / len(self.y_test)
            * np.sum(
                2
                * np.abs(self.y_pred - self.y_test)
                / (np.abs(self.y_test) + np.abs(self.y_pred))
            )
        )