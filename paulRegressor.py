from sklearn import linear_model, ensemble
from sklearn.ensemble import RandomForestRegressor,ExtraTreesRegressor,BaggingRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import Lasso,ElasticNet,LinearRegression,Ridge,SGDRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import MultiTaskElasticNet as MultiElasticNet
from sklearn.linear_model import MultiTaskLasso as MultiLasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA,SparsePCA, MiniBatchSparsePCA,TruncatedSVD
# from sklearn.grid_search import GridSearchCV,RandomizedSearchCV,ParameterGrid
from sklearn.kernel_ridge import KernelRidge
# from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from sklearn.utils.validation import check_array
from sklearn.model_selection import cross_val_predict
#from sklearn_extensions.non_negative_garotte import NonNegativeGarrote as NNGarrotteRegressor
#from sklearn_extensions.kernel_regression import KernelRegression as KernelRegressor
from sklearn.dummy import DummyRegressor

def check_arrays(array):
    if array.ndim==1:
        return check_array(array.reshape(-1,1))

    return check_array(array)

#def linearSVR(C=1.0):
#    return SVR(kernel='linear',C=1.0)

#def rbfSVR(C=1e3,gamma=0.1):
#    return SVR(kernel='rbf',C=1e3, gamma=0.1)

#def polySVR(C=1e3,degree=2):
#    return SVR(kernel='poly',C=1e3)

def NonLinearRegressor(degree):
    return make_pipeline(PolynomialFeatures(degree), Ridge())


def gradientBoost():
    params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 1,
          'learning_rate': 0.01, 'loss': 'ls'}
    return ensemble.GradientBoostingRegressor(**params)
'''
This is my package called paulRegressor completely based on sklearn but just to simplify regression tasks.
It uses 9 popular algorithms.

1. RFRegressor: http://goo.gl/MAzfcZ
2. linearSVR : tweak C http://goo.gl/gvUjUj
3. rbfSVR : tweak C and gamma http://goo.gl/gvUjUj
4. polySVR : tweak C and degree http://goo.gl/gvUjUj
5. gradientBoost: http://goo.gl/VrvBUK
6. Ridge: http://goo.gl/8xpy5D
7. Lasso: http://goo.gl/lGVeDq
8. ElasticNet: http://goo.gl/sxkf3W
9. SGDR: SGDRegressor http://goo.gl/QmI6bM
'''
