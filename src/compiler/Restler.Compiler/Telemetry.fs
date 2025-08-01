﻿// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

module Restler.Telemetry

//Instrumentation key is from app insights resource in Azure Portal
let [<Literal>] InstrumentationKey = ""

// Note: telemetry is flushed synchronously after top-level started and finished events.
// There are very few such events sent, and this allows consistently getting started
// events even if RESTler exits early.
type TelemetryClient(machineId: System.Guid, instrumentationKey: string, 
                     environmentMetadata: (string*string) list) =
    let client =
        let c = Microsoft.ApplicationInsights.TelemetryClient(
                    new Microsoft.ApplicationInsights.Extensibility.TelemetryConfiguration(instrumentationKey))
        // Make sure to not send any instance names or IP addresses
        // These must be non-empty strings to override sending the values obtained by the framework
        c.Context.Cloud.RoleName <- "none"
        c.Context.Cloud.RoleInstance <- "none"
        c.Context.Location.Ip <- "0.0.0.0"
        c

    member __.RestlerStarted(version, task, executionId, featureList) =
        client.TrackEvent("restler started",
            dict ([
                "machineId", sprintf "%A" machineId
                "version", version
                "task", task
                "executionId", sprintf "%A" executionId
            ]@environmentMetadata@featureList))
        client.Flush()

    member __.RestlerFinished(version, task, executionId, status,
                              specCoverageCounts,
                              bugBucketCounts, 
                              featureList) =
        client.TrackEvent("restler finished",
            dict ([
                "machineId", sprintf "%A" machineId
                "version", version
                "task", task
                "executionId", sprintf "%A" executionId
                "status", sprintf "%A" status
            ]@bugBucketCounts@specCoverageCounts@featureList))
        client.Flush()

    member __.ResultsAnalyzerFinished(version, task, executionId, status) =
        client.TrackEvent("results analyzer finished",
            dict ([
                "machineId", sprintf "%A" machineId
                "version", version
                "task", task
                "executionId", sprintf "%A" executionId
                "status", sprintf "%A" status
            ]))

    member __.RestlerDriverFailed(version, task, executionId) =
        client.TrackEvent("restler failed",
            dict ([
                "machineId", sprintf "%A" machineId
                "version", version
                "task", task
                "executionId", sprintf "%A" executionId]))
        client.Flush()

    interface System.IDisposable with
        member __.Dispose() =
            client.Flush()
