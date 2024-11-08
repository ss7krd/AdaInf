#include <bits/stdc++.h>
#include<stdio>
#include<iostream>
#include<math.h>
#include<inferenceFiles.h>
using namespace std;

vector<double>applicationsSLO;
map<int,vector<double>>applicationsBatchSizeLatency;
map<int,int>applicationBatchSizeMapping;
map<int,double>applicationGPUSpaceNecessity;
map<int,double>applicationGPUFractionMapping;
map<int,vector<int>>applicationEachModelAccuracyMapping[10];
map<int,vector<int>>applicationEachModelPerBatchLatency[10];
map<int,int>applicationEachModelHowMuchRetrainTime[10];
map<int,int>applicationEachModelBestExitModel[10];
map<int,int>applicationEachModelDegreeOfImpact[10];
vector<double>howManyRequests;
map<int,int>applicationHowManyModelsMapping;
map<int,int>applicationModelRetrainingRequired[10];
total_gpu_space_necessity = 0;

__global__
void applicationRunning(CUcontext *context, int id, int totalNumThreadsThisContext){
	if (id == 0){
		inferenceServing(&context, id, applicationBatchSizeMapping[id], totalNumThreadsThisContext);
		retraining(&context, id, applicationBatchSizeMapping[id], totalNumThreadsThisContext);
	}
}
__global__
void inferenceServing(CUcontext *context, int id, int batchSize, int totalNumThreadsThisContext){
	const int streamNo = batchSize;
	int numThreadsPerStream = int(floor(totalNumThreadsThisContext/streamNo));
	cudaStream_t streamList[streamNo];
	int blockSize = 128;
	for (int i = 0; i < streamNo; i++){
		cudaStreamCreate(&streamList[i]);
		inferenceServingPerStream<<<blockSize, numThreadsPerStream>>>(&context, &streamList[i], id, i);
	}
}
__global__
void retraining(CUcontext *context, int id, int batchSize, int totalNumThreadsThisContext){
	const int streamNo = batchSize;
	int numThreadsPerStream = int(floor(totalNumThreadsThisContext/streamNo));
	cudaStream_t streamList[streamNo];
	int blockSize = 128;
	for (int i = 0; i < streamNo; i++){
		cudaStreamCreate(&streamList[i]);
		retrainingPerStream<<<blockSize, numThreadsPerStream>>>(&context, &streamList[i], id, i);
	}
}
int main(){
	for (int i = 0; i < applicationsSLO.size(); i++){
		currApplicationBatchSizeLatency = applicationsBatchSizeLatency[i]
		currMinimum = 10000000000
		currBatchSize = -1
		for (int j = 0; j < currApplicationBatchSizeLatency.size(); j++){
			if(currApplicationBatchSizeLatency[j] < currMinimum){
				currMinimum = currApplicationBatchSizeLatency[j]
				currBatchSize = j
			}
		}
		applicationBatchSizeMapping[i] = currBatchSize
		gpu_space_necessity = currApplicationBatchSizeLatency[currBatchSize]/applicationsSLO[i]
		applicationGPUSpaceNecessity[i] = gpu_space_necessity;
		total_gpu_space_necessity = total_gpu_space_necessity + gpu_space_necessity
	}
	for (int i = 0; i < applicationsSLO.size(); i++){
		applicationGPUFractionMapping[i] = applicationGPUSpaceNecessity[i]/total_gpu_space_necessity
	}

	for (int i = 0; i < applicationsSLO.size(); i++){
		currApplMap = applicationEachModelAccuracyMapping[i];
		for (map<int,vector<int>>::iterator itr=currApplMap.begin(); itr != currApplMap.end(); itr++){
			currModelId = itr->first;
			currExitModelsVector = itr->second;
			currMax = -100000
			currMaxId = -1
			for (int j = 0; j < currExitModelsVector.size(); j++){
				if (currExitModelsVector[j] > currMax){
					currMax = currExitModelsVector[j];
					currMaxId = j;
				}

			}
			applicationEachModelBestExitModel[i][currModelId] = currMaxId;
		}
	}

	vector<int>GPUSpaceAdjustFrom;
	vector<double>GPUSpaceAdjustFromTotalInfTime;
	vector<int>GPUSpaceAdjustTo;
	map<int,double>applicationTotalDegreeOfImpactMapping;
	for (int i = 0; i < applicationsSLO.size(); i++){
		int oneModelRetrain = 0;
		int gpuSpaceNeeded = 0;
		howManyBatches = howManyRequests[i]/applicationBatchSizeMapping[i];
		totalInferenceTime = 0;
		howManyModels = applicationHowManyModelsMapping[i];
		for (int j = 1; j <= howManyModels; j++){
			whatVersion = applicationEachModelBestExitModel[i][j];
			timePerBatch = applicationEachModelPerBatchLatency[i][j][whatVersion];
			totalTime = howManyBatches*timePerBatch;
			totalInferenceTime = totalInferenceTime + totalTime;
		}
		totalRetrainTimeRemaining = applicationsSLO[i] - totalInferenceTime;
		totalDegreeOfImpact = 0;
		for (int j = 1; j <= howManyModels; j++){
			totalDegreeOfImpact += applicationEachModelDegreeOfImpact[i][j];

		}
		applicationTotalDegreeOfImpactMapping[i] = totalDegreeOfImpact;
		for (int j = 1; j <= howManyModels; j++){
			if (applicationModelRetrainingRequired[i][j] == 1){
				oneModelRetrain = 1;
				applicationEachModelHowMuchRetrainTime[i][j] = totalRetrainTimeRemaining*(applicationEachModelDegreeOfImpact[i][j]/totalDegreeOfImpact);
				if (applicationEachModelHowMuchRetrainTime[i][j] == 0){
					gpuSpaceNeeded = 1;
				}
			}
		}
		if (oneModelRetrain == 0){
			GPUSpaceAdjustFrom.push_back(i);
			GPUSpaceAdjustFromTotalInfTime.push_back(totalInferenceTime);
		}
		if (gpuSpaceNeeded == 1){
			GPUSpaceAdjustTo.push_back(i);
		}
	}
	double totalExtraGPUFraction = 0;
	for (int i = 0; i < GPUSpaceAdjustFrom.size(); i++){
		currAppl = GPUAdjustFrom[i];
		totalExtraGPUFraction += applicationGPUFractionMapping[i]*(GPUSpaceAdjustFromTotalInfTime[i]/applicationsSLO[i]);
		applicationGPUFractionMapping[i] -= applicationGPUFractionMapping[i]*(GPUSpaceAdjustFromTotalInfTime[i]/applicationsSLO[i]);
	}
	degreeOfImpactSummation = 0;
	for (int i = 0; i < GPUSpaceAdjustTo.size(); i++){
		currAppl = GPUSpaceAdjustTo[i];
		degreeOfImpactSummation += applicationTotalDegreeOfImpactMapping[currAppl];
	}
	for (int i = 0; i < GPUSpaceAdjustTo.size(); i++){
		applicationGPUFractionMapping[i] = totalExtraGPUFraction*(applicationTotalDegreeOfImpactMapping[currAppl]/degreeOfImpactSummation);
	}



	for (int i = 0; i < applicationsSLO.size(); i++){
		currApplMap = applicationEachModelAccuracyMapping[i];
		for (map<int,vector<int>>::iterator itr=currApplMap.begin(); itr != currApplMap.end(); itr++){
			currModelId = itr->first;
			currExitModelsVector = itr->second;
			currMax = -100000
			currMaxId = -1
			for (int j = 0; j < currExitModelsVector.size(); j++){
				if (currExitModelsVector[j] > currMax){
					currMax = currExitModelsVector[j];
					currMaxId = j;
				}

			}
			applicationEachModelBestExitModel[i][currModelId] = currMaxId;
		}
	}

	for (int i = 0; i < applicationsSLO.size(); i++){
		int oneModelRetrain = 0;
		int gpuSpaceNeeded = 0;
		howManyBatches = howManyRequests[i]/applicationBatchSizeMapping[i];
		totalInferenceTime = 0;
		howManyModels = applicationHowManyModelsMapping[i];
		for (int j = 1; j <= howManyModels; j++){
			whatVersion = applicationEachModelBestExitModel[i][j];
			timePerBatch = applicationEachModelPerBatchLatency[i][j][whatVersion];
			totalTime = howManyBatches*timePerBatch;
			totalInferenceTime = totalInferenceTime + totalTime;
		}
		totalRetrainTimeRemaining = applicationsSLO[i] - totalInferenceTime;
		totalDegreeOfImpact = 0;
		for (int j = 1; j <= howManyModels; j++){
			totalDegreeOfImpact += applicationEachModelDegreeOfImpact[i][j];
		}
		for (int j = 1; j <= howManyModels; j++){
			if (applicationModelRetrainingRequired[i][j] == 1){
				applicationEachModelHowMuchRetrainTime[i][j] = totalRetrainTimeRemaining*(applicationEachModelDegreeOfImpact[i][j]/totalDegreeOfImpact);
			}
		}
	}

	const int CONTEXT_POOL_SIZE = applicationsSLO.size();
	int totalNumThreads = 163840;
	int blockSize = 256;
	CUcontext contextPool[CONTEXT_POOL_SIZE];
	for (int i = 0; i < applicationsSLO.size(); i++){
		cudaContextCreate(&contextPool[i]);
		cuda_mps_active_thread_percentage(&contextPool[i], applicationGPUFractionMapping[i]*100.0);
		double howManyThreads = floor(totalNumThreads * applicationGPUFractionMapping[i]);
		int threadsPerBlock = int(floor(howManyThreads/blockSize));
		applicationRunning<<<blockSize,threadsPerBlock>>>(&contextPool[i], i, blockSize*threadsPerBlock);
	}


	return 0;
}