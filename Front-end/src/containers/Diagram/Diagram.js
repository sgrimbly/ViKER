import React from 'react';
import classes from './Diagram.module.css';
import * as SRD from "storm-react-diagrams";
require("storm-react-diagrams/dist/style.min.css");

const diagram = () => {

// 1) setup the diagram engine
const engine = new SRD.DiagramEngine();
engine.installDefaultFactories();

// 2) setup the diagram model
const model = new SRD.DiagramModel();

// 3) create a default node
const node1 = new SRD.DefaultNodeModel("Node 1", "rgb(0,192,255)");
let port1 = node1.addOutPort("Out");
node1.setPosition(100, 100);

// 4) create another default node
const node2 = new SRD.DefaultNodeModel("Node 2", "rgb(192,255,0)");
let port2 = node2.addInPort("In");
node2.setPosition(400, 100);

// 5) link the ports
let link1 = port1.link(port2);

// 6) add the models to the root graph
model.addAll(node1, node2, link1);

// 7) load model into engine
engine.setDiagramModel(model);


  return (
    <div className={classes.Diagram}>
      <SRD.DiagramWidget diagramEngine={engine} />
    </div>
  );
}

export default diagram;
