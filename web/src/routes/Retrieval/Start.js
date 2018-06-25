import React, { PureComponent } from 'react';
import { connect } from 'dva';
import {
  Col,
  Row,
  Form,
  Input,
  DatePicker,
  Select,
  Button,
  Card,
  InputNumber,
  Radio,
  Icon,
  Tooltip,
} from 'antd';
import PageHeaderLayout from '../../layouts/PageHeaderLayout';
import styles from './style.less';

const FormItem = Form.Item;
const { Option } = Select;
const { RangePicker } = DatePicker;
const { TextArea } = Input;

@connect(({ loading }) => ({
  submitting: loading.effects['form/submitRegularForm'],
}))
@Form.create()
export default class BasicForms extends PureComponent {
  handleSubmit = e => {
    e.preventDefault();
    this.props.form.validateFieldsAndScroll((err, values) => {
      if (!err) {
        this.props.dispatch({
          type: 'form/submitRegularForm',
          payload: values,
        });
      }
    });
  };
  render() {
    const { submitting } = this.props;
    const { getFieldDecorator, getFieldValue } = this.props.form;

    const formItemLayout = {
      labelCol: {
        xs: { span: 24 },
        sm: { span: 7 },
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 12 },
        md: { span: 10 },
      },
    };

    const submitFormLayout = {
      wrapperCol: {
        xs: { span: 24, offset: 0 },
        sm: { span: 10, offset: 7 },
      },
    };

    const numrows = [1, 1, 1, 1, 1, 1, 1];
    const gridStyle = {
      width: '25%',
      textAlign: 'center',
    };
    const rowStyle = {
      marginBottom: '10px',
      textAlign: 'center',
    };
    const buttonStyle = {
      margin: '10px',
    };
    return (
      <PageHeaderLayout>
        <Row gutter={8} style={rowStyle}>
          <Col span={8}>
            {' '}
            <Card title="检索策略" />{' '}
          </Col>
          <Col span={8}>
            {' '}
            <Card title="检索目标" />{' '}
          </Col>
          <Col span={8}>
            {' '}
            <Card title="反馈次数" />{' '}
          </Col>
        </Row>
        <Row gutter={8}>
          <Col span={24}>
            <Card title="请选择最符合的人脸">
              <Card.Grid style={gridStyle}>Content</Card.Grid>
              <Card.Grid style={gridStyle}>Content</Card.Grid>
              <Card.Grid style={gridStyle}>Content</Card.Grid>
              <Card.Grid style={gridStyle}>Content</Card.Grid>
              <Card.Grid style={gridStyle}>Content</Card.Grid>
              <Card.Grid style={gridStyle}>Content</Card.Grid>
              <Card.Grid style={gridStyle}>Content</Card.Grid>
            </Card>
          </Col>
        </Row>
        <Row gutter={8} style={rowStyle}>
          <Col span={24}>
            <Button type="primary" style={buttonStyle}>
              提交
            </Button>
            <Button type="primary" style={buttonStyle}>
              提交
            </Button>
          </Col>
        </Row>
        {/* <div >
          <Row gutter={16}>
            {numrows.map((object, i) => (
              <Col span={8}>
                <Card hoverable bordered={false} height="100">
                  Card content{object}
                </Card>
              </Col>
            ))}
          </Row>
        </div> */}
      </PageHeaderLayout>
    );
  }
}
