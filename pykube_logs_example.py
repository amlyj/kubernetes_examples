
import backports.ssl_match_hostname
import pykube
pykube.http.requests.packages.urllib3.connection.match_hostname = backports.ssl_match_hostname.match_hostname

import operator

api = pykube.HTTPClient(pykube.KubeConfig.from_file("~/.kube/config"))
#pods = pykube.Pod.objects(api).filter(selector="<your-pod>")
pods = pykube.Pod.objects(api).filter(namespace="default")
#pods = filter(operator.attrgetter("ready"), pods)
pod_obj = pods.response['items'][0]
pod = pykube.Pod(api, pod_obj)
print pod.logs(timestamps=True)
