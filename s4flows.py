#!/usr/bin/python
# -*- coding:UTF-8 -*-
import httplib2
import time

class OdlUtil:
    http = httplib2.Http()	
    url = ''
    def __init__(self, host, port):
        self.url = 'http://' + host + ':' + port
    def install_flow(self, container_name='default',username="admin", password="admin"):
        self.http.add_credentials(username, password)
        flow_name = 'flow_' + str(int(time.time()*1000)) 
        h2_s4_s2_1 = '''
            {"flow-node-inventory:flow": [
            {"id": "1","flow-name": "s4_s2_1","cookie": 256,
            "hard-timeout":4,"instructions": {
            "instruction": [{"order": 0,"apply-actions": {
            "action": [{"order": 0,"output-action": {
            "output-node-connector": "2"}}]}}]},
            "priority": 1000,"table_id": 0,"match": {
            "ipv4-destination": "10.0.0.1/32","in-port": "4",
            "ethernet-match": {"ethernet-type": {"type": 2048}}}}]}
         '''

        h2_s4_s1_1 = '''
            {"flow-node-inventory:flow": [
            {"id": "0","flow-name": "s4_s2_1","cookie": 256,
            "hard-timeout":2,"instructions": {
            "instruction": [{"order": 0,"apply-actions": {
            "action": [{"order": 0,"output-action": {
            "output-node-connector": "1"}}]}}]},
            "priority": 1005,"table_id": 0,"match": {
            "ipv4-destination": "10.0.0.1/32","in-port": "4",
            "ethernet-match": {"ethernet-type": {"type": 2048}}}}]}
         '''       
        h2_s4_s3_1 = '''
            {"flow-node-inventory:flow": [
            {"id": "2","flow-name": "s4_s2_1","cookie": 256,
            "hard-timeout":3,"instructions": {
            "instruction": [{"order": 0,"apply-actions": {
            "action": [{"order": 0,"output-action": {
            "output-node-connector": "3"}}]}}]},
            "priority": 1002,"table_id": 0,"match": {
            "ipv4-destination": "10.0.0.1/32","in-port": "4",
            "ethernet-match": {"ethernet-type": {"type": 2048}}}}]}
         '''

        h3_s4_s2_1='''
            {"flow-node-inventory:flow": [
            {"id": "4","flow-name": "s4_s2_1","cookie": 256,
            "hard-timeout":4,"instructions": {
            "instruction": [{"order": 0,"apply-actions": {
            "action": [{"order": 0,"output-action": {
            "output-node-connector": "2"}}]}}]},
            "priority": 1000,"table_id": 0,"match": {
            "ipv4-destination": "10.0.0.1/32","in-port": "5",
            "ethernet-match": {"ethernet-type": {"type": 2048}}}}]}
         '''

        h3_s4_s1_1 = '''
            {"flow-node-inventory:flow": [
            {"id": "3","flow-name": "s4_s2_1","cookie": 256,
            "hard-timeout":2,"instructions": {
            "instruction": [{"order": 0,"apply-actions": {
            "action": [{"order": 0,"output-action": {
            "output-node-connector": "1"}}]}}]},
            "priority": 1005,"table_id": 0,"match": {
            "ipv4-destination": "10.0.0.1/32","in-port": "5",
            "ethernet-match": {"ethernet-type": {"type": 2048}}}}]}
         '''

        h3_s4_s3_1 = '''
          {"flow-node-inventory:flow": [
            {"id": "5","flow-name": "s4_s2_1","cookie": 256,
            "hard-timeout":3,"instructions": {
            "instruction": [{"order": 0,"apply-actions": {
            "action": [{"order": 0,"output-action": {
            "output-node-connector": "3"}}]}}]},
            "priority": 1002,"table_id": 0,"match": {
            "ipv4-destination": "10.0.0.1/32","in-port": "5",
            "ethernet-match": {"ethernet-type": {"type": 2048}}}}]}
         '''

        h4_s4_s2_1 = '''
          {"flow-node-inventory:flow": [
            {"id": "7","flow-name": "s4_s2_1","cookie": 256,
            "hard-timeout":4,"instructions": {
            "instruction": [{"order": 0,"apply-actions": {
            "action": [{"order": 0,"output-action": {
            "output-node-connector": "2"}}]}}]},
            "priority": 1000,"table_id": 0,"match": {
            "ipv4-destination": "10.0.0.1/32","in-port": "6",
            "ethernet-match": {"ethernet-type": {"type": 2048}}}}]}
         '''
        h4_s4_s1_1 = '''
          {"flow-node-inventory:flow": [
            {"id": "6","flow-name": "s4_s2_1","cookie": 256,
            "hard-timeout":2,"instructions": {
            "instruction": [{"order": 0,"apply-actions": {
            "action": [{"order": 0,"output-action": {
            "output-node-connector": "1"}}]}}]},
            "priority": 1005,"table_id": 0,"match": {
            "ipv4-destination": "10.0.0.1/32","in-port": "6",
            "ethernet-match": {"ethernet-type": {"type": 2048}}}}]}
         '''
        h4_s4_s3_1 = '''
          {"flow-node-inventory:flow": [
            {"id": "8","flow-name": "s4_s2_1","cookie": 256,
            "hard-timeout":3,"instructions": {
            "instruction": [{"order": 0,"apply-actions": {
            "action": [{"order": 0,"output-action": {
            "output-node-connector": "3"}}]}}]},
            "priority": 1002,"table_id": 0,"match": {
            "ipv4-destination": "10.0.0.1/32","in-port": "6",
            "ethernet-match": {"ethernet-type": {"type": 2048}}}}]}
         '''
        
        headers = {'Content-type': 'application/json'}
        num=0
        while num < 4 :
            response, content = self.http.request(uri='http://192.168.81.133:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/0', body=h2_s4_s1_1, method='PUT',headers=headers)
            response, content = self.http.request(uri='http://192.168.81.133:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/1', body=h2_s4_s2_1, method='PUT',headers=headers)
            response, content = self.http.request(uri='http://192.168.81.133:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/2', body=h2_s4_s3_1, method='PUT',headers=headers)
            response, content = self.http.request(uri='http://192.168.81.133:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/3', body=h3_s4_s1_1, method='PUT',headers=headers)
            response, content = self.http.request(uri='http://192.168.81.133:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/4', body=h3_s4_s2_1, method='PUT',headers=headers)
            response, content = self.http.request(uri='http://192.168.81.133:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/5', body=h3_s4_s3_1, method='PUT',headers=headers)
            response, content = self.http.request(uri='http://192.168.81.133:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/6', body=h4_s4_s1_1, method='PUT',headers=headers)
            response, content = self.http.request(uri='http://192.168.81.133:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/7', body=h4_s4_s2_1, method='PUT',headers=headers)
            response, content = self.http.request(uri='http://192.168.81.133:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/8', body=h4_s4_s3_1, method='PUT',headers=headers)
            print("success")
            time.sleep(4)
            print(content.decode())


if __name__=='__main__':
	
	odl = OdlUtil('192.168.81.133', '8181')
	odl.install_flow()