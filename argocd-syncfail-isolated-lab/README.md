# Isolated Argo CD SyncFail hook lab

This lab uses its own Argo CD Application and namespace. The `success` source
creates a stable ConfigMap; the `failure` source adds a ConfigMap with a
non-string `data` value, which Kubernetes rejects during apply. The failed
sync should execute the `SyncFail` Job and leave its completed status and logs
available for inspection.

The Application initially points at `success`. After this directory is
available on the configured Git remote, install it and wait for the baseline
sync:

```powershell
kubectl apply -f argocd-syncfail-isolated-lab/application.yaml
argocd app sync syncfail-isolated-lab
argocd app wait syncfail-isolated-lab --sync --health
```

Switch only this Application to the deliberately failing source and start a
new sync operation:

```powershell
kubectl -n argocd patch application syncfail-isolated-lab --type merge -p '{"spec":{"source":{"path":"argocd-syncfail-isolated-lab/failure"}}}'
argocd app sync syncfail-isolated-lab
```

The second sync is expected to fail. Verify the operation and hook independently:

```powershell
argocd app get syncfail-isolated-lab
kubectl -n syncfail-isolated-lab get job syncfail-proof
kubectl -n syncfail-isolated-lab get job syncfail-proof -o jsonpath='{.status.succeeded}'
kubectl -n syncfail-isolated-lab logs job/syncfail-proof
```

The evidence is a failed Argo CD operation, a completed `syncfail-proof` Job,
and the `SYNCFAIL_HOOK_EXECUTED` marker in its logs. Keep the Application and
namespace after verification. To remove only this lab when explicitly desired:

```powershell
kubectl delete -f argocd-syncfail-isolated-lab/application.yaml
kubectl delete namespace syncfail-isolated-lab
```
